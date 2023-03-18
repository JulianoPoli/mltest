#!/usr/bin/env python

import platform, psutil, os
import requests
import time

api_url = 'http://127.0.0.1:1235'

# Valida se a api está online e envia os dados
def send_data_to_api(json_data):
    try:
        r = requests.get(f'{api_url}/status', timeout=3)
        hc_resp = int(r.status_code)
    except requests.exceptions.RequestException:
        hc_resp = int(500)

    if hc_resp != 200:
        print(f'[!] Api {api_url} offline!')
    else:
        print(f'[+] Send Info to {api_url}!')
        r = requests.post(f'{api_url}/information', json=json_data)


# Monta o Json para enviar via API
def json_builder(os_name, os_version, system_users, os_ps, sys_cpu, cpu_status, sys_ram):
    json_payload = [
    {
        "os_name":os_name,
        "os_version":os_version,
        "system_users":f"{system_users}",
        "os_ps":f"{os_ps}",
        "sys_cpu":sys_cpu,
        "cpu_status":cpu_status,
        "sys_ram":sys_ram
    }]
    return json_payload

# Captura as informações do sistema
class sys_info_get():
    def os_name(self):
        return str(platform.system())

    def os_version(self):
        return platform.release()
    
    def system_users(self):
        users = []
        for user in psutil.users():
            users.append(f"{user.name}")
        return users

    def os_ps(self):
        all_ps = []
        for process in psutil.process_iter ():
            Name = process.name()
            ID = process.pid
            all_ps.append(f'{ID} - {Name}')
        return all_ps

    def sys_cpu(self):
        return platform.processor()
    
    def cpu_status(self):
        load1, load5, load15 = psutil.getloadavg() 
        cpu_usage = f'{(round((load15/os.cpu_count()) * 100))}%'
        return cpu_usage

    def sys_ram(self):
        memory_info = f'{(round(psutil.virtual_memory().free / (1024.0 **2)))}GB of {(round(psutil.virtual_memory().total / (1024.0 **2)))}GB'
        return memory_info

SystemInfo = sys_info_get()

while True:
    json_data = (json_builder(SystemInfo.os_name(), SystemInfo.os_version(), SystemInfo.system_users(), SystemInfo.os_ps(), SystemInfo.sys_cpu(), SystemInfo.cpu_status(), SystemInfo.sys_ram()))
    send_data_to_api(json_data)
    time.sleep(5)

