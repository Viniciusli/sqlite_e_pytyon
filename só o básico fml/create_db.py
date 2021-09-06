import sqlite3

# se 'clientes.db' não existir, o comando cria o arquivo
conn = sqlite3.connect("clientes.db")

# sempre desconecte
conn.close()
