import sqlite3

db = sqlite3.connect('prod.db')
reader = db.cursor()

# lendo os dados
reader.execute("SELECT * FROM logs;")

for linha in reader.fetchall():

    print(f"\n\n[+] Logs of: {linha[0]} {linha[1]} {linha[4]} \n    Ram use: {linha[6]}\n    Processor Usage: {linha[5]}\n    Sys Users: {linha[2]} \n\n All process: {linha[3]}")

db.close()