# -*- coding: utf-8 -*-
'''
Created on 6 maj 2018
@author: Albert Defler
'''
from time import sleep
import urllib.request
import json

class SoundOfText:
    '''Class to get pronunciations from soundoftext.com service REST API.'''
    
    def __init__(self):
        self.url = 'https://api.soundoftext.com/'
       
    def _get_headers(self):
        return {'Content-Type': 'application/json'}
        
    def _post_request(self, path, data):
        url = self.url + path
        params = json.dumps(data).encode(encoding='utf_8')
        headers = self._get_headers()
        return urllib.request.Request(url = url, data = params, headers = headers)

    def _get_request(self, path, id):
        url = self.url + path + '/' + id
        headers = self._get_headers()
        return urllib.request.Request(url = url, headers = headers)
        
    def _get_order_status(self, id):
        '''Use this operation to get the current status of the requested sound
           and to retrieve the public url for the mp3 file or error message.
          
            GET /sounds/:id
            
            Response
            On Success
            First the sound will be pending if the server has not finished fulfilling the request.

            {
              "status": "Pending"
            }
            
            Once the request has been fulfilled, you will receive a "Done" status and the public url for the mp3 file.

            {
              "status": "Done",
              "location": "https://hostname/path/to/audio.mp3"
            }
            
            If something went wrong fulfilling the request, you will receive an error status and a message.

            {
              "status": "Error",
              "message": "Failed to create sound due to..."
            }
        '''
        content = None
        path = 'sounds'
        req = self._get_request(path, id)
        # try 3 times check status
        for i in range(3):
            response = urllib.request.urlopen(req)
            content = response.read()
            content = json.loads(content)
            if content['status'].upper() in ['DONE','ERROR']:
                break # exit loop if order is finished
            sleep(2) #sleep 2 sec
        return content
    
    def order_conversion(self, text, language):
        '''Sends POST request of conversion text to voice.
            
            POST /sounds
            
            Use this operation to create a new sound.
            Currently the engine parameter is ignored, 
            but it is included because more engines might be used in the future.
            Both voice and text are required parameters.
    
            Response
            On Success
            An HTTP status code of 200 with response body:

            {
              "success": true,
              "id": "<RFC4122 uuid>"
            }
            IDs look like this: "416eda90-552e-11e7-9a60-63d42f732a9c".

            On Failure
            An HTTP status code of 400 or 500 with response body:

            {
              "success": false,
              "message": "Request failed due to..."
            }
        
        '''
        request_body = {"engine": "Google",
                        "data": {
                            "text": text,
                            "voice": language
                            }
                        }
        req = self._post_request('sounds', request_body)
        response = urllib.request.urlopen(req)
        content = response.read()
        return json.loads(content)
    
    def get_audio_url(self, id):
        '''Gets url of audio file or raise exception if there is conversion error
        
            Once the request has been fulfilled, you will receive a "Done" status
            and the public url for the mp3 file.

            {
              "status": "Done",
              "location": "https://hostname/path/to/audio.mp3"
            }
            
            If something went wrong fulfilling the request, you will receive an error status and a message.

            {
              "status": "Error",
              "message": "Failed to create sound due to..."
            }
        '''
        
        order_status = self._get_order_status(id)
        status = order_status['status'].upper()
        if 'DONE' == status:
            return order_status['location']
        elif 'ERROR' == status:
            raise Exception(order_status['message'])
        elif 'PENDING' == status:
            raise Exception('Text2Audio downloader timeout: order still pending')
        else:
            raise Exception('Text2Audio downloader: unsupported case')
            
    def download_file(self, url):
        return urllib.request.urlretrieve(url)