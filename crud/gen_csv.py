import io
import sys
import datetime
import names
from gen_random_values import *

lista = []
repeat = 100

with io.open('csv/clientes.csv', 'w') as f:
    for i in range(repeat):
        fname = names.get_first_name()
        lname = names.get_last_name()
        name = fname + ' ' + lname
        email = fname[0].lower() + '.' + lname.lower() + '@email.com'
        c = gen_cities()
        city = c[0]
        uf = c[1]
        # nome, idade, cpf, email, fone, cidade, uf, criado_em
        lista.append(
            (name, gen_age(), gen_cpf(), email,
             gen_fone(), city, uf, gen_timestamp())
        )

    for l in lista:
        s = l[0] + ',' + str(l[1]) + ',' + l[2] + ',' + l[3] + \
            ',' + l[4] + ',' + l[5] + ',' + l[6] + ',' + l[7] + '\n'
        f.write(str(s))
