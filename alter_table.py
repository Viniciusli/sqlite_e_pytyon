from os import curdir
import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# adiciona uma nova coluna na tabela clientes
cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""")

conn.commit()
print("Novo campo adicionado com sucesso")
conn.close()
