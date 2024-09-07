from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Carregador(Base):
    __tablename__ = 'carregador'

    id = Column("pk_carregador", Integer, primary_key=True)
    modelo = Column(String(140), unique=False)
    fabricante = Column(String(140), unique =False)
    quantidade = Column(Integer)
    bairro = Column(String(140), unique =False)
    cidade = Column(String(140), unique =False)
    estado = Column(String(140), unique =False)
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o carregador e o comentário.
    # Essa relação é implicita, não está salva na tabela 'carregador',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, modelo:str, fabricante:str, quantidade:int, bairro:str, cidade:str, estado:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Adiciona um Carregador

        Padrão:
            modelo: modelo do carregador
            fabricante: fabricante do carregador
            quantidade: quantidade disponível do carregador
            bairro: bairro onde esta localizado o carregador
            cidade: cidade onde esta localizado o carregador
            estado: estado onde esta localizado o carregador
            data_insercao: data de quando o carregador foi adicionado no banco de dados
        """
        self.modelo = modelo
        self.fabricante = fabricante
        self.quantidade = quantidade
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

        # Se a data não for inserida, será a data do momento em que o carregador foi adicionado
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Carregador
        """
        self.comentarios.append(comentario)        

