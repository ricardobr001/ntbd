# Cria o keyspace
CREATE KEYSPACE ntbd WITH REPLICATION = {'class':'SimpleStrategy','replication_factor':1};

# Cria a tabela
CREATE TABLE compras(
    produto_1 varchar,
    quantidade_1 int,
    preco_1 float,
    produto_2 varchar,
    quantidade_2 int,
    preco_2 float,
    nome varchar,
    cpf varchar,
    PRIMARY KEY(cpf)
);

# Importa dados do .csv
COPY compras(produto_1, quantidade_1, preco_1, produto_2, quantidade_2, preco_2, nome, cpf)
FROM 'dados-cassandra.csv'
WITH DELIMITER='|';