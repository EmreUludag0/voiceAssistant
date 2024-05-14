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
    playsound(voice)
    os.remove(voice)

talking("sizin için ne yapabilirim?")
print("konusun")


voice = listening()
talking(voice)
print(voice)
os.remove(voice)


"""""
def yanit(ses):
    if "merhaba" in ses:
        konusma("size de merhaba")

        

while True:
    ses = dinleme()
    print(ses)

    if bool(ses) == True:
        print(ses)
        ses = ses.lower()
        yanit(ses)
    
 """""


