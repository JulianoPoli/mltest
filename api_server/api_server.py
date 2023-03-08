from flask import Flask,jsonify,request
import sqlite3
import pandas as pd

db = sqlite3.connect('prod.db', check_same_thread=False)
  
app =   Flask(__name__)
  
@app.route('/information', methods=['POST'])
def information():
    request_data = request.get_json()
    request_data = list(request_data)
    print(request_data)
    mont_data = pd.DataFrame(request_data)
    mont_data.to_sql(name = 'logs', con = db, if_exists = 'append', index = False)

    return "Ok"

@app.route('/status', methods=['GET'])
def status():
    return "Ok"
    
if __name__=='__main__':
    app.run(debug=False, port=1235, host="127.0.0.1")