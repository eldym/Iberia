import mysql.connector
import json

def get_config():
    with open('config.json') as f:
        return json.load(f)

config = get_config()

class Database():
    def __init__(self):
        self.db = mysql.connector.connect(host=config["db_host"],user=config["db_user"],passwd=config["db_pass"],database=config["db_name"])

        

    