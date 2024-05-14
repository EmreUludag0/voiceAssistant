from googletrans import Translator
import sys
import speech_recognition as sr
from playsound import playsound #playsound hata verirse powershel'i yonetici olarak baslattıktan sonra kaldırıp tekrar yuklenmesi gerekebilir.
from gtts import gTTS
import os


record = sr.Recognizer()
translator = Translator() 


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
    
def turkishToEnglish(text):
    translatedText = translator.translate(text, src="tr", dest="en")
    return translatedText.text        

talking("lütfen konuşun")
print("Konusun")



while True:
    voice = listening()
    
    if bool(voice) == True:
        print(voice)
        translatedText = turkishToEnglish(voice)
        talking(translatedText)
        #os.remove(voice)



