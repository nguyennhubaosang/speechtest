
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize, build_table_schema
import flat_table

###
import speech_recognition as sr     
r = sr.Recognizer()
with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout= 3, phrase_time_limit= 3)

try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

###

app_id = "82cc5758"
app_key = "abde664b38ee6e7930e239b11690565e"

endpoint = "entries"
language_code = "en-us"
word_id = r.recognize_google(audio)


url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})


## Result
print("code {}\n".format(r.status_code))
#print("text \n" + r.text)

#print("json \n" + json.dumps(r.json(), indent= 4, sort_keys=True))

data = json.dumps(r, separators=(',', ':'), sort_keys=True, indent= 3) 
print(data)
