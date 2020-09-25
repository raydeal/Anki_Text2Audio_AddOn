# -*- coding: utf-8 -*-
'''
Created on 6 maj 2018
@author: Albert Defler
'''
import os

from anki.hooks import addHook #wrap
from aqt import mw, QIcon
from aqt.editor import Editor
from aqt.utils import showInfo, showCritical

from .downloader import SoundOfText
from .utils import create_new_file_name, remove_uploaded_file

default_text_source = ''
default_audio_language = ''

def get_audio(editor):
    
    if 'front' == default_text_source.lower():
        source_text = editor.note.fields[0].lower()
        editor.web.eval("focusField(%d);" % 0) #set focus to field where media will be added
    else:
        source_text = editor.note.fields[1].lower()
        editor.web.eval("focusField(%d);" % 1) #set focus to field where media will be added
        
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
            media_folder = os.path.join(editor.mw.pm.profileFolder(), "collection.media")
            new_file_name = create_new_file_name(old_file_name, source_text, media_folder)
            if new_file_name:
                os.rename(old_file_name, new_file_name)
                #save to media folder, set audio in note and remove original file
                editor.addMedia(new_file_name, canDelete = True)
            else:
                #remove downloaded file
                remove_uploaded_file(old_file_name)
            editor.mw.progress.finish()
    else:
        showCritical(result['message'], title = 'Text2Audio download error')
    

# Definition of the new button
def mySetupButtons(buttons, editor):
    # Place were we keep icons
    #icons_dir = os.path.join(self.mw.pm.addonFolder(), 'text2audio_addon', 'icons')
    
    #download_audio_btn = editor._addButton("download_audio", lambda ed=self: get_audio(ed),
    #                    tip="Translate Text to Audio")
    # download_audio_btn.setIcon(QIcon(os.path.join(icons_dir, 'download_audio.png')))
    icons_dir = os.path.join(mw.pm.addonFolder(), 'text2audio', 'icons', 'download_audio.png')
    editor._links["text2audio"] = get_audio
    download_audio_btn = [editor._addButton(icons_dir, "text2audio",
                        tip="Translate Text to Audio")]
    return buttons + download_audio_btn

def init():
    # Concatenate Editor.setupButtons with mySetupButtons
    # So that a new button is inserted into the Editor
    # Editor.setupButtons = wrap(Editor.setupButtons, mySetupButtons)
    addHook("setupEditorButtons", mySetupButtons)
