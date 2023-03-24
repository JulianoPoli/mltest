
## Contexto
Levando como base a ideia de criar uma API e um Agent para monitoramento e armazenamento de logs de sistemas Linux utilizando Python, desenvolvi estas aplicações!

O Agent captura as informações da máquina Linux, realiza um tratamento da informação para o formato JSON e as envia para a API.

Informações capturadas pelo script:
- Informações sobre o processador. 
- Lista de processos em execução. 
- Usuários com sessão aberta no sistema. 
- Nome do sistema operacional. 
- Versão do sistema operacional.
- Informações sobre o uso de RAM. 

A API recebe as informações enviadas pelo Agent e as grava em um banco de dados MySQL




## Requisitos

Requisitos minimos para execução das respectivas aplicações:

Agent:
```bash
$ sudo apt-get install python3
$ cd agent
$ pip install -r requirements.txt
```

Api Server:
```bash
$ sudo apt-get install python3
$ cd api_server
$ pip install -r requirements.txt
```

## Como executar

Agent:
```bash
$ cd agent
$ python3 agent.py
```

Api Server:
```bash
$ docker-compose build
$ docker-compose up
```
