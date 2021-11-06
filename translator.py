import requests

class Translator:
    __url = ""
    __app_id = ""
    __app_key = ""

    def __init__(self, url, app_id, app_key):
        self.__url = url
        self.__app_id = app_id
        self.__app_key = app_key

    def translate(self, text):
        url = self.__url + "/api/v2/entries/en-us/" + text
        req = requests.get(url, headers = {"app_id": self.__app_id, "app_key": self.__app_key})

        if req.status_code == 200:
            return req.json()

        raise ValueError("Fail to call api")
