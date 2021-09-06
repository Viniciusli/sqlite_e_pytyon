import sqlite3
import io

conn = sqlite3.connect('clientes_recuperados.db')
cursor = conn.cursor()

f = io.open('clientes_dump.sql', 'r')
sql = f.read()
f.close()
cursor.executescript(sql)

print('Banco de dados recuperado com sucesso')
print('salvo como clientes_recuperados.db')

conn.close()
