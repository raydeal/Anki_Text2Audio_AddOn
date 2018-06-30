# Anki - Text to Audio Converter

Anki-Text to Audio is an Add-On for the flashcard program [Anki](https://apps.ankiweb.net/).

This Add-On automates of conversion text to audio by using [Sound of Text](https://soundoftext.com/) API.

It adds sound only to one side of flashcard: Front or Back (you can change it in settings of add-on (see Default Values))

### Available Languages:
For list of languages and supported codes of voices please see [Sound of Text doc](https://soundoftext.com/docs#index)

## Usage
When Add-On is installed properly you will see an extra button 
![Image of Text2Audio](https://github.com/raydeal/Anki_Text2Audio_AddOn/blob/master/docs/img/text2audio.png)

So if you want to add sound to a flashcard field you can click on the button and let it to do that for you.

## Default Values
You can change the default values for text source and audio language. Just chahege the values 
of the variables in the file 'text2audio.py'. You can find the file in the Add-Ons Folder of your Anki Installation.

```
core.default_text_source = "back"
core.default_audio_language = "en-GB" # English (United Kingdom)
```

## Installation
You can download this project and copy the 'text2audio.py' file and the 'text2audio_addon' folder into your Anki Add-On directory.
