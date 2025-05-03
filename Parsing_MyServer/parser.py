import requests
from Parsing_MyServer.session import Session
from typing import Optional

class Parser:
    url_data_serv = 'http://150.241.90.208:2020/s4xbnZr6ylHkKoB/server/status'
    url_data_user = 'http://150.241.90.208:2020/s4xbnZr6ylHkKoB/panel/inbound/list'

    def __init__(self):
        self.ses = Session()

    @staticmethod
    def bytes_to_gigabytes(bytes: int) -> float:
        return round(bytes/(1024**3), 2)
        
    def get_data_serv(self):
        if self.ses.session.post(url=__class__.url_data_serv, cookies=self.ses.cookie).status_code != 200:
            self.ses = Session()
        data = self.ses.session.post(url=__class__.url_data_serv, cookies=self.ses.cookie).json()['obj']
        return {
            'cpu': round(data['cpu'], 2),
            'mem': self.bytes_to_gigabytes(data['mem']['current']),
            'disk': self.bytes_to_gigabytes(data['disk']['current'])
        }

    def get_data_user(self, user: Optional[str] = None):
        if user is not None and user not in self.get_users():
            raise Exception('The user was not found')
        if self.ses.session.post(url=__class__.url_data_serv, cookies=self.ses.cookie).status_code != 200:
            self.ses = Session()
        responce_json = self.ses.session.post(url=__class__.url_data_user, cookies=self.ses.cookie).json()
        data_dict = responce_json['obj'][0]['clientStats']
        data = {
            user['email']: {
                'upload': self.bytes_to_gigabytes(user['up']), 
                'dowload': self.bytes_to_gigabytes(user['down']), 
                'trafic': self.bytes_to_gigabytes(user['up'] + user['down'])
                } for user in data_dict
            }
        return data if user is None else data[user]
    
    def get_users(self) -> list:
        if self.ses.session.post(url=__class__.url_data_serv, cookies=self.ses.cookie).status_code != 200:
            self.ses = Session()
        responce_json = self.ses.session.post(url=__class__.url_data_user, cookies=self.ses.cookie).json()
        data_dict = responce_json['obj'][0]['clientStats']
        return [user['email'] for user in data_dict]

def main():
    data = Parser()
    print(data.get_data_serv())

if __name__ == '__main__':
    main()

