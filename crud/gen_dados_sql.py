import sqlite3
import names
import io
from gen_random_values import *


lista = []
with io.open('sql/clientes_dados.sql', 'wt') as f:
    f.write("INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em) VALUES\n")
    for i in range(20):
        fname = names.get_first_name()
        lname = names.get_last_name()
        name = fname + ' ' + lname
        email = fname[0].lower() + '.' + lname + '@email.com'
        c = gen_cities()
        cidade = c[0]
        uf = c[1]
        lista.append(
            (name, gen_age(), gen_cpf(), email,
             gen_fone(), cidade, uf, gen_timestamp())
        )
    for dado in lista:
        f.write(str(dado)+",\n")
