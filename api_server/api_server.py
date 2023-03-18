from flask import Flask,jsonify,request
import sqlite3
import pandas as pd
from jsonschema import validate

db = sqlite3.connect('prod.db', check_same_thread=False)
app =   Flask(__name__)

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
        mont_data.to_sql(name = 'logs', con = db, if_exists = 'append', index = False)
        print(request_data[0])
        return "OK", 200
    except:
        return "Json Payload Error", 400
    

@app.route('/status', methods=['GET'])
def status():
    return "Ok"
    
if __name__=='__main__':
    app.run(debug=False, port=1235, host="127.0.0.1")