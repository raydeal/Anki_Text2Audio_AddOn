# -*- coding: utf-8 -*-
'''
Created on 6 maj 2018
@author: Albert Defler

# Anki Text to Audio Add-on
# Helps creating audio for flashcards translates text to audio using https://soundoftext.com/ web API.
# https://soundoftext.com/docs#index
#
# https://github.com/raydeal/Anki_Text2Audio_AddOn
# 
#
# Copyright (C) 2018  Albert Defler
#
'''

import text2audio_addon.core as core

# Here you can set the default settings.
# For supported codes of voices you can see https://soundoftext.com/docs#index
core.default_text_source = "back"
core.default_audio_language = "en-GB" # English (United Kingdom)

core.init()