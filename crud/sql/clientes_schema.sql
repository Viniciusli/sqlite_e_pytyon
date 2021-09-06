CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL UNIQUE,
    fone TEXT,
    cidade TEXT,
    uf VARCHAR(2) NOT NULL,
    criado_em DATETIME NOT NULL
);