import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()
nome_tabela = 'clientes'

# obtem informações da tabela
cursor.execute(f"PRAGMA table_info({nome_tabela})")

colunas = [tupla[1] for tupla in cursor.fetchall()]
print("Colunas: %s", colunas)
print("-"*100)

# listando as tabelas do bd
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""")

print("tabelas: ")
for tabela in cursor.fetchall():
    print("%s" % (tabela))
print("-"*100)

# obtem o schema da tabela
cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""", (nome_tabela,))

print("Schema: ")
for schema in cursor.fetchall():
    print('%s' % (schema))

conn.close()
