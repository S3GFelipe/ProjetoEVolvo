# BACKEND

# Passo a passo via terminal de como acessar a documentação  da API 

1. Criação do ambiente virtual

```
python -m venv env
.\env\Scripts\Activate
```

2. Instalação das bibliotecas necessárias para o funcionamento da API no diretório raiz

```
(env)$ pip install -r requirements.txt
```

3. Execução e reinicialização da API

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

4. Acessar a URL referente a documentação

Acesso da documentação via [http://localhost:5000/#/](http://localhost:5000/#/) no navegador 


Sobre o Docker

Como executar através do Docker
Certifique-se de ter o Docker instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile no terminal e seus arquivos de aplicação e Execute como administrador o seguinte comando para construir a imagem Docker:
```
$ docker build -t api .
```
Uma vez criada a imagem, para executar o container basta executar, como administrador, seguinte o comando:
```
$ docker run -d -p 5000:5000 api
```
Uma vez executando, para acessar a API, basta abrir no navegador:
```
http://localhost:5000/#/ 
```
Alguns comandos úteis do Docker

Para verificar se a imagem foi criada, você pode executar o seguinte comando:
```
$ docker images
```
Caso queira remover uma imagem, basta executar o comando:
```
$ docker rmi <IMAGE ID>
```
Substituindo o IMAGE ID pelo código da imagem

# FRONTEND

Para visualizar o front, basta fazer o download de todos os arquivos presente no diretório do Git Hub e abrir o arquivo "index.html", dessa forma já é possível visualizar toda a construção do front-end.

Para verificar se o container esta em execução você pode executar o seguinte comando:
```
$ docker container ls --all
```

Sobre o Docker

Como executar através do Docker
Certifique-se de ter o Docker instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile no terminal e seus arquivos de aplicação e Execute como administrador o seguinte comando para construir a imagem Docker:
```
$ docker build -t front .
```
Uma vez criada a imagem, para executar o container basta executar, como administrador, seguinte o comando:
```
$ docker run -d -p 8080:80 front
```
Uma vez executando, para acessar o front-end, basta abrir o http://localhost:8080/#/ no navegador.


API's externas utilizadas:

- SheetJS: Essa API será utilizada para baixar em um arquivo em excel a lista de carregadores apresentados na página HTML.
Sobre a API: É uma API pública, gratuita, sem licença de uso e que não é necessário um cadastro para utilização
Mais informações sobre a API: https://github.com/SheetJS/sheetjs

- ViaCEP: Essa API será utilizada para receber informações de endereço com base no CEP inserido pelo usuário
Sobre a API: É uma API pública, gratuita, sem licença de uso e que não é necessário um cadastro para utilização
Mais informações sobre a API:https://viacep.com.br/  

