import requests
from Parsing_MyServer.config import login, password

class Session:
    data = {
        "username" : login,
        "password" : password
    }
    url = 'http://150.241.90.208:2020/s4xbnZr6ylHkKoB/login'
    def __init__(self):
        self.session = requests.Session()
        response = self.session.post(__class__.url, data=__class__.data)
        self.cookie = response.cookies
