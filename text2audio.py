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
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import text2audio_addon.core as core

# Here you can set the default settings.
# For supported codes of voices you can see https://soundoftext.com/docs#index
core.default_text_source = "back"
core.default_audio_language = "en-GB" # English (United Kingdom)

core.init()