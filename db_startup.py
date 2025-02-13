import json
import mysql.connector

from database import Database

def get_config():
    with open('config.json') as f:
        return json.load(f)

config = get_config()

HB_HOST=config["db_host"]
DB_USER=config["db_user"]
DB_PASS=config["db_pass"]
DB_NAME=config["db_name"]

class database_startup():

    def mysql_db_create():
        db = mysql.connector.connect(host=HB_HOST,user=DB_USER,passwd=DB_PASS)
        cursor = db.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

    def mysql_tables_create():
        try: db = mysql.connector.connect(host=HB_HOST,user=DB_USER,passwd=DB_PASS,database=DB_NAME)
        except Exception as e: print(f"Error getting database!\nException:",e)
        else: 
            cursor = db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS warns (id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT, criminal_uuid DECIMAL(20,0) NOT NULL, inquisitor_uuid DECIMAL(20,0) NOT NULL, content VARCHAR(64))")
    
try: db = mysql.connector.connect(host=HB_HOST,user=DB_USER,passwd=DB_PASS,database=DB_NAME)
except: 
    try: 
        database_startup.mysql_db_create()
        database_startup.mysql_tables_create()
    except Exception as e: print(f"Error connecting to MySQL!\nException:",e)
    else:print(f"DB successfully created!")
else: print(f"Error: DB already exists!")