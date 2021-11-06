import speech_recognition as sr     

class Converter:
    # def __init__(self):

    def listen(self):
        r = sr.Recognizer()
        # New Process for listening
        with sr.Microphone() as source:
            print("Please, say something !!!")
            audio = r.listen(source)

        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            raise ValueError("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            raise ValueError("Could not request results from Google Speech Recognition service; {0}".format(e))