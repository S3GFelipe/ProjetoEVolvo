from pydantic import BaseModel
from typing import Optional, List
from model.carregador import Carregador

from schemas import ComentarioSchema


class CarregadorSchema(BaseModel):
    """ Define como um novo carregador deve ser representado na lista
    """
    modelo: str = "Carregador DC de 150 kW"
    fabricante: str = "XCharger"
    quantidade: Optional[int] = 1
    bairro: str = "Tatuapé"
    cidade: str = "São Paulo"
    estado: str = "SP"

class EditarCarregadorSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca para edição da despesa. 
    """
    modelo: Optional[str] = ""
    fabricante: Optional[str] = ""
    quantidade: Optional[str] = None
    bairro: Optional[str] = ""
    cidade: Optional[str] = ""
    estado: Optional[str] = ""


class CarregadorBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca por carregadores no banco de dados. 
    Que será feita apenas com base no modelo.
    """
    carregador_id: Optional[int]  # Manter a busca por ID
    bairro: Optional[str]  # Adicionar busca por bairro
    cidade: Optional[str]  # Adicionar busca por cidade
    estado: Optional[str]  # Adicionar busca por estado
    
    


class ListagemCarregadoresSchema(BaseModel):
    """ Define como a lista carregadores cadastrados no estoque será apresentada.
    """
    carregadores:List[CarregadorSchema]


def apresenta_carregadores(carregadores: List[Carregador]):
    """ Retorna uma representação do carregador cadastrado no estoque seguindo o schema definido em 
    CarregadorViewSchema.
    """
    result = []
    for carregador in carregadores:
        result.append({
            "id": carregador.id,
            "modelo": carregador.modelo,
            "fabricante": carregador.fabricante,
            "quantidade": carregador.quantidade,
            "bairro": carregador.bairro,
            "cidade": carregador.cidade,
            "estado": carregador.estado,
        })

    return {"carregadores": result}


class CarregadorViewSchema(BaseModel):
    """ Define como um carregador será retornado:
    """
    id: int = 1
    modelo: str = "Carregador DC de 150 kW"
    fabricante: str = "WEG"
    quantidade: Optional[int] = 1
    bairro: str = "Tatuape"
    cidade: str = "São Paulo"
    estado: str = "SP"
    comentarios:List[ComentarioSchema]
    

class CarregadorDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção de um carregador do estoque.
    """
    carregador_id: Optional[int]  # Manter a busca por ID


def apresenta_carregador(carregador: Carregador):
    """ Retorna uma representação do carregador cadastrado no estoque seguindo o 
        schema definido em CarregadorViewSchema.
    """
    return {
        "id": carregador.id,
        "modelo": carregador.modelo,
        "fabricante": carregador.fabricante,
        "quantidade": carregador.quantidade,
        "bairro": carregador.bairro,
        "cidade": carregador.cidade,
        "estado": carregador.estado,
        "total_cometarios": len(carregador.comentarios),
        "comentarios": [{"texto": c.texto} for c in carregador.comentarios]
    }
