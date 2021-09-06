import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

id_cliente = '2'

# exclui um registro da tabela
cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente))

conn.commit()
print("Registro exluido com sucesso")
conn.close()
