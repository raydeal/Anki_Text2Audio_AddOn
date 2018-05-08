# -*- coding: utf-8 -*-
'''
Created on 6 maj 2018
@author: Albert Defler
'''
import os
import sys

from anki.hooks import wrap
from aqt.editor import Editor
from aqt.utils import showInfo, showCritical

from .downloader import SoundOfText

PROFILE_HOME = os.path.expanduser("~/Documents/Anki/User 1")

#from GUI.TranslatorDialog import TranslatorDialog
default_text_source = ''
default_audio_language = ''

def get_audio(editor):

    if 'front' == default_text_source.lower():
        source_text = editor.note.fields[0].lower()
    else:
        source_text = editor.note.fields[1].lower()
        
    source_text = source_text.replace('&nbsp;',' ')   

    sot = SoundOfText()
    result = sot.order_conversion(source_text, default_audio_language)

    if result['success']:
        editor.mw.progress.start(label=_("Downloading..."),immediate=True)
        audio_id = result['id']
        audio_url = None
        try:
            audio_url = sot.get_audio_url(audio_id)
        except Exception as e:
            editor.mw.progress.finish()
            showCritical(str(e), title = 'Text2Audio download error')
        else:
            #download MP3 file
            download_result = sot.download_file(audio_url)
            #rename file before copy
            old_file_name = download_result[0]
            new_file_name = os.path.join(os.path.dirname(old_file_name), '{}.mp3'.format(source_text.strip().rstrip('?!').replace(' ','_')))
            os.rename(old_file_name, new_file_name)
            #save to media folder and set audio in note
            editor.addMedia(unicode(new_file_name,'utf-8'), canDelete = True)
            #remove tmp file
            os.remove(new_file_name)
            editor.mw.progress.finish()
    else:
        showCritical(result['message'], title = 'Text2Audio download error')
    

# Definition of the new button
def mySetupButtons(self):
    self._addButton("Get Audio", lambda ed=self: get_audio(ed),
                    text="A", tip="Translate Text to Audio (Ctrl+A)", key="Ctrl+a")


def init():
    # Concatenate Editor.setupButtons with mySetupButtons
    # So that a new button is inserted into the Editor
    Editor.setupButtons = wrap(Editor.setupButtons, mySetupButtons)
