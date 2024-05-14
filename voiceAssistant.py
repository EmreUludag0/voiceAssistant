import pyaudio
import sys
import speech_recognition as sr
from playsound import playsound #playsound hata verirse powershel'i yonetici olarak baslattıktan sonra kaldırıp tekrar yuklenmesi gerekebilir.
from gtts import gTTS
import os


record = sr.Recognizer()


def listening(a=False):
    with sr.Microphone() as source: #mikrofon açmak için kulladım.
        if a:
            print(a)
        microphone = record.listen(source)
        voice = ""       

        try: 
            voice = record.recognize_google(microphone, language = "tr-TR")
        except sr.UnknownValueError: # bilinmeyen deger
            print("Asistan: anlasilmadi")
        except sr.RequestError: # 
            print("Asistan: Hata")
        
        
        return voice

def talking(metin):
    tts = gTTS(text = metin, lang="tr", slow=False)
    voice = "konusma.mp3"
    tts.save(voice)
    #playsound(voice)
    playsound(voice)
    os.remove(voice)
    
def answer(voice):
    if "merhaba" in voice:
        talking("Size de merhaba")
        

talking("Sizin için ne yapabilirim?")
print("Konusun")



while True:
    voice = listening()
    
    if bool(voice) == True:
        print(voice)
        voice = voice.lower()
        talking(answer(voice))
        #answer(voice)
        #os.remove(voice)


""""" #while döndusunun ustunde yer alir

voice = listening()
talking(voice)
print(voice)
os.remove(voice)

"""""

"""""
def answer(voice):
    if "merhaba" in ses:
        talking("size de merhaba")

        

while True:
    ses = dinleme()
    print(ses)

    if bool(ses) == True:
        print(ses)
        ses = ses.lower()
        yanit(ses)
    
 """""


