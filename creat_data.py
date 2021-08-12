import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Regis', 35, '00000000000', 'regis@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2014-07-30')
""")
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Anderson Bruno Araújo Santos', 15, '12300000000', 'anderson@email.com', '5320-0000', 'São Paulo', 'SP', '2014-08-01')
""")
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Danilo de Jesus Santos', 20, '12300000001', 'danilo@email.com', '5320-0001', 'São Paulo', 'SP', '2014-08-01')
""")
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Matheus', 19, '33333333333', 'matheus@email.com', '11-98765-4324', 'Campinas', 'SP', '2014-06-08')
""")

conn.commit()

print("Dados inseridos com sucesso!")
conn.close()
