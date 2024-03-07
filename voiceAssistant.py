import speech_recognition as sr

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
    
print("konusabilirsin")    
ses = dinleme()

print(ses)












