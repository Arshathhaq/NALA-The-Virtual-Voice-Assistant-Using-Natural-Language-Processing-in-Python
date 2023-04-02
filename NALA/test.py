from NALA import *


def ActiveListening():
        r= sr.Recognizer()
        with sr.Microphone() as source :
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            print("\nListening.....")
            voice = r.listen(source)
            try:
                print("Processing.....")
                word =  r.recognize_google(voice)
                print("you said : " + word)
            except Exception as e:
                print("sorry, can You repeat again?")
                speech.speak("sorry, can You repeat again?") 
                return ActiveListening()
        return word
ActiveListening()