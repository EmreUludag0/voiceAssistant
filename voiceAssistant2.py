import speech_recognition as sr
from playsound import playsound # playsound hata verdigi icin powershel'i yonetici olarak baslatip kaldırıp tekrar yuklenmesi gerekebilir.
from gtts import gTTS
import os


kayit = sr.Recognizer()


def dinleme(a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon = kayit.listen(kaynak)
        ses = ""
 
        try: 
            ses = kayit.recognize_google(mikrofon, language = "tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadim")
        except sr.RequestError:
            print("Asistan: Sistem şu anda çalismiyo")
        
        return ses

def konusma(metin):
    tts = gTTS(text = metin, lang="tr", slow=False)
    ses = "konusma.mp3"
    tts.save(ses)
    playsound(ses)
    os.remove(ses)



print("konusabilirsin")    
ses = dinleme()

print(ses)
konusma(ses)











