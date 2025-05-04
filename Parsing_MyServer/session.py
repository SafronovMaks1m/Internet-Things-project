import requests
import os
from dotenv import load_dotenv

load_dotenv()
class Session:
    data = {
        "username" : os.getenv('PARSER_USERNAME'),
        "password" : os.getenv('PARSER_PASSWORD')
    }
    url = 'http://150.241.90.208:2020/s4xbnZr6ylHkKoB/login'
    def __init__(self):
        self.session = requests.Session()
        response = self.session.post(__class__.url, data=__class__.data)
        self.cookie = response.cookies
