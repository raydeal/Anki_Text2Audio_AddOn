# -*- coding: utf-8 -*-
'''
Created on 24 October 2020
@author: Albert Defler
#
# Anki Text to Audio Add-on
# Helps creating audio for flashcards translates text to audio using https://soundoftext.com/ web API.
# https://soundoftext.com/docs#index
#
# https://github.com/raydeal/Anki_Text2Audio_AddOn
# 
# Anki version >= 2.1.20
#
# Copyright (C) 2020  Albert Defler
#
'''
from aqt import mw
from . import core

# Here you can set the default settings.
# For supported codes of voices you can see https://soundoftext.com/docs#index
config = mw.addonManager.getConfig(__name__)
text_source=config['text_source']
audio_language=config['audio_language']
core.default_text_source = text_source  # "back"
core.default_audio_language = audio_language  # "en-GB" # English (United Kingdom)

core.init()


