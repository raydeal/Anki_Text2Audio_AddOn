# -*- coding: utf-8 -*-
'''
Created on 27 maj 2018
@author: Albert Defler
'''

import os

def crc16(text):
    '''
    CRC-16 - ANSI Algorithm
    '''
    crc = 0x0000
    for i in range(len(text)):
        crc = ord(text[i]) ^ crc;
        for j in range(8):
            if (crc & 1) == 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1;
    return crc

def crc16_to_str(crc):
    return '{0:04X}'.format(crc)

def create_new_file_name(old_file_name, source_text, media_dir):
    if not source_text:
        return None
    
    file_name_format = '{}.mp3'
    #remove chars !?,.:;'"
    trans_table = {ord(c): None for c in '!?,.:;\'"'}
    full_file_name = source_text.translate(trans_table)
    #substitute multiple whitespace with single space char
    #truncate white chars from both sites and replace space char by underscore
    #everything is done in one line
    full_file_name = '_'.join(full_file_name.split())
    #we assume that file name will not be longer than 30 chars before adding CRC16 if duplicate
    if len(full_file_name) > 30:
        underscore_indx = full_file_name.rindex('_',1,25) 
        slice_file_name = full_file_name[:underscore_indx]
    else:
        slice_file_name = full_file_name
        
    #check if file exists in media directory
    if os.path.isfile(os.path.join(media_dir,file_name_format.format(slice_file_name))):
        #add CRC16 sum to the file name to make unique name
        file_crc16 = crc16(full_file_name)
        file_name = file_name_format.format(slice_file_name + '_' + crc16_to_str(file_crc16))
        #check if such file name exists
        if os.path.isfile(os.path.join(media_dir,file_name)):
            raise Exception('File {0} already exists'.format(file_name))
    else:
        file_name = file_name_format.format(slice_file_name)
    
    new_file_name = os.path.join(os.path.dirname(old_file_name), file_name)
    return new_file_name

def remove_uploaded_file(file_name):
    os.unlink(file_name)
