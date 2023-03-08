import sqlite3

conn = sqlite3.connect('prod.db')
table_build = conn.cursor()
table_build.execute("CREATE TABLE logs (os_name text,os_version text, system_users text,os_ps text,sys_cpu text,cpu_status text,sys_ram text)")


print('Create')
conn.close()