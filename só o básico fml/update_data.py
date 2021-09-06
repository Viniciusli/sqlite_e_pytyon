from os import curdir
import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

nome_cliente = 'vinicius'
novo_fone = '91-9-9888-4545'
novo_criado_em = '2021-08-12'

cursor.execute("""
UPDATE clientes
SET fone = ?, criado_em = ?
WHERE nome = ?
""", (novo_fone, novo_criado_em, nome_cliente))

conn.commit()
conn.close()
