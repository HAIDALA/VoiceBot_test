import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from time import ctime
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            VoiceBot_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="fr-FR")
        except sr.UnknownValueError:
            VoiceBot_speak("Désolé, je n'ai pas compris")
        except sr.RequestError:
            VoiceBot_speak('désolé mon service est en panne')
        return voice_data

def VoiceBot_speak(audio_string):
    tts = gTTS(text=audio_string, lang='fr')
    r = random.randint(1, 1000000)
    audio_file = 'audio' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    
    
    if 'recherche' in voice_data:
        search = record_audio('quel produit recherchez-vous?')
        url = 'https://herboristerie-principale.ma/?s='+ search +'&page=search&post_type=product'
        
        webbrowser.get().open(url)
        VoiceBot_speak("voici ce que j'ai trouvé pour " + search)
    
    if 'au revoir' in voice_data:
        VoiceBot_speak('au revoir! à la prochaine')
        exit()

time.sleep(1)
VoiceBot_speak("Je suis ici pour vous aider à trouver le produit que vous voulez, s'il vous plaît, si vous voulez rechercher un produit, dites Recherche")
while 1:  
    voice_data = record_audio()
    respond(voice_data)