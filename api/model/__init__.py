from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from model.base import Base
from model.comentario import Comentario
from model.carregador import Carregador

db_path = "database/"
# Faz a verificação se o diretório existe
if not os.path.exists(db_path):
   # Se não existir, o diretório é criado
   os.makedirs(db_path)

# URL que permite o acesso ao banco
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# A engine é criada para realizar uma conexão com o banco
engine = create_engine(db_url, echo=False)

# O criador de seção com o banco é instanciado
Session = sessionmaker(bind=engine)

# Caso o banco não exista, ele é criado 
if not database_exists(engine.url):
    create_database(engine.url) 

# Caso as tabelas do banco não existam, elas serão criadas
Base.metadata.create_all(engine)
