import os
import mysql.connector
import pandas as pd
from flask import Flask, jsonify, request
from jsonschema import validate
from mysql.connector import Error
from sqlalchemy import create_engine

def get_mysql_sqlachemy_engine():
    try:   
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_port = os.environ.get('DB_PORT')
        database = os.environ.get('DB_NAME')

        sqlEngine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{database}', pool_recycle=3600)
        return sqlEngine
    
    except Error as e:
        print("Error while connecting to MySQL", e)

db_engine = get_mysql_sqlachemy_engine()
app = Flask(__name__)

#Define o formato de JSON aceito pela API
schema = {
    "type": "object",
    "properties": {
        "os_name":{"type": "string"},
        "os_version":{"type": "string"},
        "system_users":{"type": "string"},
        "os_ps":{"type": "string"},
        "sys_cpu":{"type": "string"},
        "cpu_status":{"type": "string"},
        "sys_ram":{"type": "string"}
    },
    "required": ["os_name","os_version","system_users","os_ps","sys_cpu","cpu_status","sys_ram"],
}

@app.route('/information', methods=['POST'])
def information():
    request_data = request.get_json()
    try:
        validate(instance=request_data[0], schema=schema)
        mont_data = pd.DataFrame(request_data)
        mont_data.to_sql(name = 'logs', con = db_engine, if_exists = 'append', index = False)
        print(request_data[0])
        return "OK", 200
    except Exception as e:
        print(e)
        return "Json Payload Error", 400
    

@app.route('/status', methods=['GET'])
def status():
    return "Ok"
    
if __name__=='__main__':
    app.run(debug=False, port=1235, host="0.0.0.0")