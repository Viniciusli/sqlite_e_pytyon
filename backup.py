import sqlite3
import io

conn = sqlite3.connect('clientes.db')

with io.open('clientes_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)

print('backup realizado com sucesso')
print('salvo como clientes_dump.sql')

conn.close()
