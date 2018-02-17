-- Bases de dados OLAP


CREATE TABLE dim_cliente (
  fk_cliente int NOT NULL,
  cod_cliente int default NULL,
  nome varchar(50) default NULL,
  telefone varchar(100) default NULL,
  sexo varchar(9)  default NULL,
  estado_civil varchar(20) default NULL,
  endereco varchar(40)  default NULL,
  data_inicial date default NULL,
  data_final date default NULL,
  versao int default NULL,
  PRIMARY KEY  (fk_cliente)
);



CREATE TABLE dim_produto (
  fk_produto int NOT NULL,
  codigo_produto int default NULL,
  descricao varchar(30) default NULL,
  linha varchar(30)  default NULL,
  fornecedor varchar(50)  NOT NULL,
  PRIMARY KEY  (fk_produto)
);


CREATE TABLE dim_regiao (
  fk_regiao int NOT NULL,
  cidade varchar(50) default NULL,
  estado varchar(2) default NULL,
  regiao varchar(20)default NULL,
  PRIMARY KEY  (fk_regiao)
); 

CREATE TABLE dim_tempo (
  fk_tempo int NOT NULL,
  mes int default NULL,
  trimestre int default NULL,
  ano int default NULL,
  data date default NULL,
  descmes varchar(3) default NULL,
  PRIMARY KEY  (fk_tempo)
); 

CREATE TABLE  dim_vendedor (
  fk_vendedor int NOT NULL,
  vendedor varchar(20) default NULL,
  vlr_comissao float default NULL,
  cod_vendedor int default NULL,
  PRIMARY KEY  (fk_vendedor)
) ;

CREATE TABLE fato_pedidos (
  fk_cliente int NOT NULL,
  fk_produto int NOT NULL,
  fk_regiao int NOT NULL,
  fk_tempo int NOT NULL,
  fk_vendedor int NOT NULL,
  qtd_venda int NOT NULL,
  vlr_venda float NOT NULL
) ;