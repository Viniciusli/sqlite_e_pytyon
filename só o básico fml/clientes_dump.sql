BEGIN TRANSACTION;
CREATE TABLE clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL, 
    fone TEXT,
    cidade TEXT,
    uf VARCHAR(2) NOT NULL,
    criado_em DATE NOT NULL
, bloqueado BOOLEAN);
INSERT INTO "clientes" VALUES(1,'Regis',35,'00000000000','regis@email.com','11-98765-4321','Sao Paulo','SP','2014-07-30',NULL);
INSERT INTO "clientes" VALUES(3,'Danilo de Jesus Santos',20,'12300000001','danilo@email.com','5320-0001','São Paulo','SP','2014-08-01',NULL);
INSERT INTO "clientes" VALUES(4,'Matheus',19,'33333333333','matheus@email.com','11-98765-4324','Campinas','SP','2014-06-08',NULL);
INSERT INTO "clientes" VALUES(5,'Fabio',23,'44444444444','fabio@email.com','1234-5678','Belo Horizonte','MG','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(6,'Joao',21,'55555555555','joao@email.com','11-1234-5600','Sao Paulo','SP','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(7,'Xavier',24,'66666666666','xavier@email.com','12-1234-5601','Campinas','SP','2014-06-10',NULL);
INSERT INTO "clientes" VALUES(8,'vinicius',18,'10101012121','vinicius@email.com','91-9-9888-4545','Belem','PA','2021-08-12',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',8);
COMMIT;
