# config.py: config
import json

class config:
    config=None

    def __init__(self):
        file = open('config.json', encoding='utf-8')
        self.config=json.load(file)
    
    def mysql(self):
        return {'host': self.config['mysql'][0]['host'], 'username': self.config['mysql'][0]['username'],'password': self.config['mysql'][0]['password'] , 'database': self.config['mysql'][0]['database']}
    
    def salt(self):
        return self.config['auth'][0]['salt']

def __init__():
    pass