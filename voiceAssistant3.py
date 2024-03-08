#hata alıyorum, tekrar bakıcam
import speech_recognition as sr
from playsound import playsound #playsound hata verirse powershel'i yonetici olarak baslattıktan sonra kaldırıp tekrar yuklenmesi gerekebilir.
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

def yanit(ses):
    if "merhaba" in ses:
        konusma("size de merhaba")
    if "çıkış" in ses:
        konusma("cikis yapiliyor")
        quit()



konusma("merhaba Emre")
print("dinliyorum")

while True:
    ses = dinleme()
    if bool(ses) == True:
        print(ses)
        ses = ses.lower()
        yanit(ses)


ses = dinleme()

print(ses)
konusma(ses)











