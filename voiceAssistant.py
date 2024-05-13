import pyaudio
import speech_recognition as sr
from playsound import playsound #playsound hata verirse powershel'i yonetici olarak baslattıktan sonra kaldırıp tekrar yuklenmesi gerekebilir.
from gtts import gTTS
import os


kayit = sr.Recognizer()


def dinleme(a=False):
    with sr.Microphone() as kaynak: #mikrofon açmak için kulladım.
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""
 
        try: 
            ses = kayit.recognize_google(mikrofon, language = "tr-TR")
        except sr.UnknownValueError: # bilinmeyen deger
            print("Asistan: anlasilmadi")
        except sr.RequestError: # 
            print("Asistan: Hata")
        
        return ses

def konusma(metin):
    tts = gTTS(text = metin, lang="tr", slow=False)
    ses = "konusma.mp3"
    tts.save(ses)
    playsound(ses)
    os.remove(ses)

konusma("sizi dinliyorum")
ses = dinleme()
print(ses)

def yanit(ses):
    #ses = ses.lower() # sonradan ekledim. hata çıkabilir.
    if "merhaba" in ses:
        konusma("size de merhaba")
    if "çıkış" in ses:
        konusma("çıkış yapiliyor")
        


while True:
    ses = dinleme()
    if bool(ses) == True:
        print(ses)
        ses = ses.lower()
        yanit(ses)
    



