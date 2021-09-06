import os
from posixpath import ismount
import sqlite3
import io
import datetime
from sqlite3.dbapi2 import Error, SQLITE_SELECT
import names
import csv
from gen_random_values import *


class Connect:
    def __init__(self, db_name: str):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print("Banco: ", db_name)
            self.cursor.execute("SELECT SQLITE_VERSION()")
            self.data = self.cursor.fetchone()
            print(f"SQLite version: {self.data}")
        except sqlite3.Error:
            print("erro ao abri banco de dados!")
            return False

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()


class ClientesDb:

    # inserir um registro
    # inserir com lista
    # inserir de arquivo
    # inserir de csv
    # inserir registros com parametros
    # inserir valores randomicos

    db_name = 'clientes'

    def __init__(self):
        self.db = Connect('clientes.db')
        self.db_name

    def create_schema(self, schema_name='sql/clientes_schema.sql'):
        print(f"Criando tabela {self.db_name} ...")
        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error as err:
            print(f"Aviso: A tabela {self.db_name} já existe", err)
            return False
        print("Tabela criada com sucesso")

    ''' CREATE '''

    def inserir_registro(self):
        try:
            self.db.cursor.execute("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES ('vinicius lee', 19, '12345678901', 'vinicius@email.com', '(91) 9999-8888', 'Belém', 'PA', '2021-08-14 18:04:00:199999')
            """)
            self.db.commit_db()
            print("registro inserido com sucesso")
        except sqlite3.IntegrityError:
            print("Aviso: Email deve ser unico")
            return False

    def inserir_com_lista(self):
        lista = [
            ('Agenor de Sousa', 23, '12345678901', 'agenor@email.com',
             '(10) 8300-0000', 'Salvador', 'BA', '2021-07-29 11:23:01.199001'),
            ('Bianca Antunes', 21, '12345678902', 'bianca@email.com',
             '(10) 8350-0001', 'Fortaleza', 'CE', '2021-07-28 11:23:02.199002'),
            ('Carla Ribeiro', 30, '12345678903', 'carla@email.com',
             '(10) 8377-0002', 'Campinas', 'SP', '2021-07-28 11:23:03.199003'),
            ('Fabiana de Almeida', 25, '12345678904', 'fabiana@email.com',
             '(10) 8388-0003', 'São Paulo', 'SP', '2021-07-29 11:23:04.199004')
        ]
        try:
            self.db.cursor.executemany("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES (?,?,?,?,?,?,?,?)
            """, lista)
            self.db.commit_db()
            print(f"Dados inseridos com sucesso: {len(lista)} registros")
        except sqlite3.IntegrityError:
            print("Aviso: Email deve ser unico")
            return False

    def inserir_de_arquivo(self):
        try:
            with open('sql/clientes_dados.sql', 'r') as f:
                dados = f.read()
                self.db.cursor.executescript(dados)
                self.db.commit_db()
                print("Dados do arquivo inseridos com sucesso")
        except sqlite3.IntegrityError:
            print("Aviso: Email deve ser unico")
            return False

    def inserir_de_csv(self, file_name: str = 'csv/clientes.csv'):
        try:
            reader = csv.reader(open(file_name, 'r'), delimiter=',')
            linha = (reader,)
            for linha in reader:
                self.db.cursor.execute("""
                INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
                VALUES (?,?,?,?,?,?,?,?)
                """, linha)
                self.db.commit_db()
                print("Dados importados de arquivo csv gravados com sucesso")
        except sqlite3.IntegrityError:
            print("Aviso: Email deve ser unico")
            return False

    def inserindo_com_parametros(self):
        self.nome = input("Nome: ").title()
        self.idade = input("Idade: ")
        self.cpf = input("CPF (sem pontos e traços): ")
        self.email = input("E-mail: ")
        self.fone = input("telefone ((xx) xxxx-xxxx): ")
        self.cidade = input("Cidade")
        self.uf = input("UF: ")
        self.criado_em = datetime.datetime.now().isoformat(' ')

        try:
            self.db.cursor.execute("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES (?,?,?,?,?,?,?,?)
            """, (self.nome, self.idade, self.cpf, self.email,
                  self.fone, self.cidade, self.uf, self.criado_em))
            self.db.commit_db()
            print("Dados inseridos com sucesso")
        except sqlite3.IntegrityError:
            print("Aviso: Email deve ser unico")
            return False

    def insert_random(self, repeat: int = 10):
        lista = []
        for _ in range(repeat):
            fnome = names.get_first_name()
            lnome = names.get_last_name()
            nome = fnome + ' ' + lnome
            email = fnome[0].lower() + '.' + lnome.lower() + '@email.com'
            c = gen_cities()
            cidade = c[0]
            uf = c[1]
            lista.append(
                (nome, gen_age(), gen_cpf(), email,
                 gen_fone(), cidade, uf, datetime.datetime.now().isoformat(' '))
            )
        try:
            self.db.cursor.executemany("""
            INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
            VALUES (?,?,?,?,?,?,?,?)
            """, lista)
            self.db.commit_db()
            print(f"Inserindo {repeat} registros aleatórios na tabela")
        except sqlite3.IntegrityError:
            print("Aviso: Email deve ser unico")
            return False

    ''' READ 
        ler todos os clientes
        imprimir todos os clientes
        localizar cliente por id
        imprimir cliente
        contar cliente
        contar cliente por idade
        localizar cliente por idade
        localizar cliente por uf
        select personalizado
        select atraves de arquivo externo
    '''

    def ler_todos_clientes(self):
        sql = 'SELECT * FROM clientes ORDER BY nome'
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    def imprimir_todos_clientes(self):
        lista = self.ler_todos_clientes()
        print('{:>3s} {:20s} {:<5s} {:15s} {:21s} {:14s} {:15s} {:s} {:s}'.format(
            'id', 'nome', 'idade', 'cpf', 'email', 'fone', 'cidade', 'uf', 'criado_em'))
        for c in lista:
            print('{:3d} {:23s} {:2d} {:s} {:>25s} {:s} {:15s} {:s} {:s}'.format(
                c[0], c[1], c[2],
                c[3], c[4], c[5],
                c[6], c[7], c[8]))

    def localizar_cliente(self, id: int):
        find_cliente = self.db.cursor.execute(
            'SELECT * FROM clientes WHERE id = ?', (id,)
        )
        return find_cliente.fetchone()

    def imprimir_cliente(self, id: int):
        if self.localizar_cliente(id) == None:
            print("não existe cliente com o id informado")
        else:
            print(self.localizar_cliente(id))

    def contar_clientes(self):
        n_clientes = self.db.cursor.execute(
            'SELECT COUNT(*) FROM clientes'
        )
        print("Total de clientes: ", n_clientes.fetchone()[0])

    def contar_clientes_por_idade(self, idade: int = 50):
        c = self.db.cursor.execute(
            "SELECT COUNT(*) FROM clientes WHERE idade > ?", (idade,)
        )
        print(f"Clientes maiores que {idade} anos: {c.fetchone()[0]}")

    def localizar_clientes_por_idade(self, idade: int = 50):
        clientes = self.db.cursor.execute(
            "SELECT * FROM clientes WHERE idade > ?", (idade,)
        )
        print(f"Clientes maiores que {idade} anos: ")
        for cliente in clientes.fetchall():
            print(cliente)

    def localizar_clientes_por_uf(self, uf: str = 'PA'):
        clientes = self.db.cursor.execute(
            "SELECT * FROM clientes WHERE uf = ?", (uf,)
        )
        print(f"Clientes do estado: {uf}")
        for cliente in clientes.fetchall():
            print(cliente)

    def my_select(self, sql: str = "SELECT * FROM clientes WHERE uf = 'AM';"):
        clientes = self.db.cursor.execute(sql)
        self.db.commit_db()
        print("Clientes do estado AM")
        for cliente in clientes.fetchall():
            print(cliente)

    def select_externo(self, file_name="sql/clientes_sp.sql"):
        with open(file_name, 'r') as f:
            dados = f.read()
            sqlcomandos = dados.split(';')
            print("Consulta feita a partir de uma arquivo externo")
            for comando in sqlcomandos:
                r = self.db.cursor.execute(comando)
                for c in r.fetchall():
                    print(c)
        self.db.commit_db()

    " UPDATE "

    def atualizar_fone(self, id):
        try:
            cliente = self.localizar_cliente(id)
            if cliente:
                self.novo_fone = input("Novo fone: ")
                self.db.cursor.execute("""
                UPDATE clientes
                SET fone = ?
                WHERE id = ?
                """, (self.novo_fone, id,)
                )
                self.db.commit_db()
                print("Dados atualizados com sucesso")
            else:
                print("Não existe cliente com o id informado")
        except Error:
            raise Error

    " DELETE "

    def deletar_cliente(self, id):
        try:
            cliente = self.localizar_cliente(id)
            if cliente:
                self.db.cursor.execute("""
                DELETE FROM clientes WHERE id = ?
                """, (id,))
                self.db.commit_db()
                print(f"Registro {id} excluido com sucesso")
            else:
                print("Não existe cliente com o id informado")
        except Error:
            print(Error)

    # adiciona uma nova coluna chamada bloqueado
    def alterar_tabela(self):
        try:
            self.db.cursor.execute("""
            ALTER TABLE clientes
            ADD COLUMN bloqueado BOOLEAN 
            """)
            self.db.commit_db()
            print("Novo campo adicionado com sucesso")
        except sqlite3.OperationalError:
            print("Aviso: O campo 'bloqueado' já existe")
            return False

    # ler informações do db
    def table_infos(self):
        t = self.db.cursor.execute(f"""
        PRAGMA table_info({self.db_name})
        """)
        colunas = [tupla[1] for tupla in t.fetchall()]
        print("Colunas: ", colunas)

    # lista as tabelas
    def table_list(self):
        tabelas = self.db.cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
        """)
        print("Tabelas: ")
        for tabela in tabelas.fetchall():
            print("%s" % (tabela))

    def table_schema(self):
        # obtem o schema da tabela
        s = self.db.cursor.execute("""
        SELECT sql FROM sqlite_master WHERE type='table' AND name=?
        """, (self.db_name,))

        print("Schema: ")
        for schema in s.fetchall():
            print("%s" % (schema))

    'FAZENDO BACKUP DO BANCO DE DADOS (EXPORTANDO DADOS)'

    def backup(self, file_name: str = 'sql/clientes_bkp.sql'):
        with io.open(file_name, 'w') as f:
            for linha in self.db.conn.iterdump():
                f.write("%s\n" % (linha))

        print("Backup feito com sucesso")
        print(f"Salvo como: {file_name}")

    "RECUPERANDO O BANCO DE DADOS (IMPORTANDO DADOS)"

    def importa_dados(self, db_name: str = 'clientes_recovery.db', file_name: str = 'sql/clientes_bkp.sql'):
        try:
            self.db = Connect(db_name)
            f = io.open(file_name, 'r')
            sql = f.read()
            self.db.cursor.executescript(sql)
            print("Banco de dados recuperado com sucesso")
            print(f"Salvo como {db_name}")
        except sqlite3.OperationalError:
            print(
                f"Aviso: o banco de dados {db_name} já existe. Exclua-o e faça novamente!")
            return False

    def fechar_conexao(self):
        self.db.close_db()


class PessoaDB:
    """A clasee pessoa representa uma pessoa no banco de dados"""

    tb_name = 'pessoa'

    def __init__(self) -> None:
        self.db = Connect('pessoas.db')
        self.tb_name

    def criar_schema(self, schema_name: str = 'sql/pessoas_schema.sql'):
        print(f"Criando tabela {self.tb_name}")

        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print(f"Aviso: a tabela {self.tb_name} já existe")
            return False

    ''' CREATE '''

    def inserir_de_csv(self, file_name: str = 'csv/cidade.csv'):
        try:
            c = csv.reader(
                open(file_name, 'rt'), delimiter=','
            )
            t = (c,)
            for t in c:
                self.db.cursor.execute("""
                INSERT INTO cidade (cidade, uf)
                VALUES (?,?)
                """, t)
            self.db.commit_db()
            print("Dados importados do csv com sucesso")
        except sqlite3.IntegrityError:
            print("Aviso: A cidade deve ser única.")
            return False

    def gen_cidades(self):
        '''conta quantas estão cadastradas e escolhe uma delas pelo id'''
        sql = 'SELECT COUNT(*) FROM cidade'
        q = self.db.cursor.execute(sql)
        return q.fetchone()[0]

    def inserir_randomico(self, repeat: int = 10):
        lista = []
        for _ in range(repeat):
            fname = names.get_first_name()
            lname = names.get_last_name()
            email = fname[0].lower() + '.' + lname.lower() + '@email.com'
            cidade_id = random.randint(1, self.gen_cidades())
            lista.append((fname, lname, email, cidade_id))
        try:
            self.db.cursor.executemany("""
            INSERT INTO pessoas (nome, sobrenome, email, cidade_id)
            VALUES (?,?,?,?)
            """, lista)
            self.db.commit_db()
            print(f"Inserindo {repeat} registros na tabela...")
            print("Registros criados com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: Email deve ser unico")
            return False

    # read_all_peaple
    def ler_todas_pessoas(self):
        sql = 'SELECT * FROM pessoas INNER JOIN cidade ON pessoas.cidade_id = cidade.id'
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    # print_all_people
    def imprimir_todas_pessoas(self):
        lista = self.ler_todas_pessoas()
        for c in lista:
            print(c)

    # my select, imprime todos os nome que começam com 'r'
    def my_select(self, sql: str = "SELECT * FROM pessoas WHERE nome LIKE 'R%' ORDER BY nome;"):
        r = self.db.cursor.execute(sql)
        self.db.commit_db()
        print("Nomes que começam com R: ")
        for c in r.fetchall():
            print(c)

    def table_list(self):
        # lista as tabelas do bd
        l = self.db.cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
        """)
        print("Tabelas: ")
        for tabela in l.fetchall():
            print("%s" % (tabela))

    def fechar_conexao(self):
        self.db.close_db()


if __name__ == "__main__":
    #    c = ClientesDb()

    '''create'''
#    c.create_schema()
#    c.inserir_de_registro()
#    c.inserir_com_lista()
#    c.inserir_de_arquivo()
#    c.inserir_de_csv()
#    c.inserindo_com_parametros()
#    c.insert_random()

    '''read'''
#    c.imprimir_todos_clientes()
#    c.imprimir_cliente(id=10)
#    c.contar_clientes()
#    c.contar_clientes_por_idade()
#    c.localizar_clientes_por_idade()
#    c.localizar_clientes_por_uf()
#    c.my_select()
#    c.select_externo()

    '''update'''
#    c.atualizar_fone(100)

    '''delete'''
#    c.deletar_cliente(id=9)

    '''alterar tabela'''
#    c.alterar_tabela()

    '''infos da tabela'''
#    c.table_list()

    '''schema da tabela'''
#    c.table_schema()

    '''exportando dados'''
#    c.backup()

    '''importando dados'''
#    c.importa_dados()

#    c.fechar_conexao()

    p = PessoaDB()

#    p.criar_schema()
#    p.inserir_de_csv()
#    p.inserir_randomico()
#    p.imprimir_todas_pessoas()
#    p.my_select()
#    p.table_list()

    p.fechar_conexao()
