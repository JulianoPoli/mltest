from flask import Flask,jsonify,request
  
app =   Flask(__name__)
  
@app.route('/information', methods=['POST'])
def information():
    request_data = request.get_json()
    request_data = request_data[0]

    os_name = request_data['os_name']
    os_version = request_data['os_version']
    system_users = request_data['system_users']
    os_ps = request_data['os_ps']
    sys_cpu = request_data['sys_cpu']
    cpu_status = request_data['cpu_status']
    sys_ram = request_data['sys_ram']
    
    print(os_name)
    print(os_version)
    print(system_users)
    print(os_ps)
    print(sys_cpu)
    print(cpu_status)
    print(sys_ram)
    
    return "Ok"

@app.route('/status', methods=['GET'])
def status():
    return "Ok"
    
if __name__=='__main__':
    app.run(debug=False, port=1234, host="127.0.0.1")