from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote
from flask_cors import CORS
from flask import redirect
from model import Session, Carregador, Comentario
from schemas import *
from logger import logger
from sqlalchemy import or_
from fastapi import HTTPException

info = Info(title="MVP Felipe Andrade", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
carregador_tag = Tag(name="Carregador", description="Adição, visualização e remoção de carregadores no banco de dados")
comentario_tag = Tag(name="Comentario", description="Adição de um comentário a um carregador cadastrado no banco de dados")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi/swagger')


@app.post('/carregador', tags=[carregador_tag],
          responses={"200": CarregadorViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_carregador(form: CarregadorSchema):
    """Adiciona um novo Carregador no banco de dados

    Retorna uma representação dos carregadores associados.
    """
    carregador = Carregador(
        modelo=form.modelo,
        fabricante=form.fabricante,
        quantidade=form.quantidade,
        bairro=form.bairro,
        cidade=form.cidade,
        estado=form.estado)
        

    try:
        # Conexão criada com a base
        session = Session()
        # adicionando carregador
        session.add(carregador)
        # Comando de adicionar um novo carregador na tabela
        session.commit()
        return apresenta_carregador(carregador), 200

    
    except Exception as e:
        # Para erros não previstos, temos a seguinte mensagem:
        error_msg = "Não foi possível salvar novo item!!!"
        return {"mesage": error_msg}, 400


@app.get('/carregadores', tags=[carregador_tag],
         responses={"200": ListagemCarregadoresSchema, "404": ErrorSchema})
def get_carregadores():
    """Faz a busca por todos os Carregadores cadastrados no banco de dados

    Apresenta a lista de carregadores presentes no banco de dados.
    """
    # Cria a conexão com a base
    session = Session()
    # Realiza a busca
    carregadores = session.query(Carregador).all()

    if not carregadores:
        # Caso não haja carregadores cadastrados no banco de dados
        return {"carregadores": []}, 200
    else:
        # Caso haja carregadores retorna a representação dos mesmos
        print(carregadores)
        return apresenta_carregadores(carregadores), 200


@app.get('/carregador', tags=[carregador_tag],
         responses={"200": CarregadorViewSchema, "404": ErrorSchema})
def get_carregador(query: CarregadorBuscaSchema):
    """Realiza a busca por carregadores com base em bairro, cidade, estado ou ID.

    Retorna a lista de carregadores correspondentes.
    """
    # Crie uma consulta inicial com todos os carregadores.
    session = Session()
    query_builder = session.query(Carregador)

    # Aplique filtros com base nos parâmetros de consulta.
    if query.carregador_id:
        query_builder = query_builder.filter(Carregador.id == query.carregador_id)
    if query.bairro:
        query_builder = query_builder.filter(Carregador.bairro == query.bairro)
    if query.cidade:
        query_builder = query_builder.filter(Carregador.cidade == query.cidade)
    if query.estado:
        query_builder = query_builder.filter(Carregador.estado == query.estado)

    # Execute a consulta e obtenha os resultados.
    carregadores = query_builder.all()

    if not carregadores:
        # Se não houver carregadores correspondentes, retorne uma lista vazia.
        return {"carregadores": []}, 200
    else:
        # Caso contrário, retorne a representação dos carregadores correspondentes.
        return apresenta_carregadores(carregadores), 200



@app.delete('/carregador', tags=[carregador_tag],
            responses={"200": CarregadorDelSchema, "404": ErrorSchema})
def del_carregador(query: CarregadorDelSchema):
    """Remove um Carregador do banco de dados a partir do seu ID

    Uma mensagem para confirmar a remoção aparece em seguida.
    """
    carregador_id = query.carregador_id

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Carregador).filter(Carregador.id == carregador_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Carregador removido", "ID": carregador_id}
    else:
        # se o carregador não foi encontrado
        error_msg = "Carregador não cadastrado no banco de dados!!!"
        return {"mesage": error_msg}, 404
     


@app.post('/comentario', tags=[comentario_tag],
          responses={"200": CarregadorViewSchema, "404": ErrorSchema})
def add_comentario(form: ComentarioSchema):
    """Adiciona de um novo comentário à um carregadores cadastrado na base identificado pelo id

    Retorna uma representação dos carregadores e comentários associados.
    """
    carregador_id  = form.carregador_id
    logger.debug(f"Adicionando comentários ao carregador #{carregador_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca pelo carregador
    carregador = session.query(Carregador).filter(Carregador.id == carregador_id).first()

    if not carregador:
        # se carregador não encontrado
        error_msg = "Carregador não encontrado na base :/"
        logger.warning(f"Erro ao adicionar comentário ao carregador '{carregador_id}', {error_msg}")
        return {"mesage": error_msg}, 404

    # criando o comentário
    texto = form.texto
    comentario = Comentario(texto)

    # adicionando o comentário ao carregador
    carregador.adiciona_comentario(comentario)
    session.commit()

    logger.debug(f"Adicionado comentário ao carregador #{carregador_id}")

    # retorna a representação de carregador 
    return apresenta_carregador(carregador), 200

@app.put('/carregador', tags=[carregador_tag], 
         responses={"200": CarregadorViewSchema, "404": ErrorSchema})
def edita_carregador(query:CarregadorBuscaSchema, form: EditarCarregadorSchema):
    """Atualiza um carregador com base no ID especificado, substituindo apenas os campos fornecidos no formulário."""

    carregador_id = query.carregador_id

    logger.debug(f"Atualizando dados sobre o Carregador #{carregador_id}")

      
    # Criando uma sessão do banco de dados
    session = Session()
    
    # Consulta para encontrar o carregador com o ID especificado
    carregador = session.query(Carregador).filter(Carregador.id == carregador_id).first()
    
    
    if not carregador:
        # Se o carregador não for encontrado, retorne uma resposta 404 (não encontrado)
        raise HTTPException(status_code=404, detail="Carregador não encontrado")

    # Atualize apenas os campos do carregador fornecidos no formulário, mantendo os não preenchidos inalterados
    if form.modelo is not None and form.modelo.strip() != "":
        carregador.modelo = form.modelo
    if form.fabricante is not None and form.fabricante.strip() != "":
        carregador.fabricante = form.fabricante
    if form.quantidade is not None and form.quantidade.strip() != "":
        carregador.quantidade = int(form.quantidade)
    if form.bairro is not None and form.bairro.strip() != "":
        carregador.bairro = form.bairro
    if form.cidade is not None and form.cidade.strip() != "":
        carregador.cidade = form.cidade
    if form.estado is not None and form.estado.strip() != "":
        carregador.estado = form.estado

    # Salve as alterações no banco de dados
    session.commit()

    # Retorna a representação do carregador atualizado
    return apresenta_carregador(carregador)










