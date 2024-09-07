# Projeto EVolvo por Felipe Andrade

Pensando em uma experiência do usuário personalizada para proprietários de veículos elétricos da marca Volvo, pensei em desenvolver uma aplicação que permita que os usuários possam interagir com uma aplicação, que mostre onde encontrar carregadores para veículos elétricos, facilitando a busca por esses eletropostos a fim de realizar a recarga do seu veículo.

Essa aplicação permite que os proprietários de veículos elétricos, encontrem carregadores para veículos elétricos públicos, mais próximos possíveis da sua localização. O usuário pode interagir com a aplicação adicionando carregadores, editando carregadores e deletando carregadores de uma lista. Tais ações são realizadas por meio das rotas GET, POST, PUT e DELETE no BACKEND.

Um dos componentes da aplicação consiste em um FRONTEND, onde foi desenvolvida uma interface do usuário, para que ele possa interagir com a aplicação. Foi desenvolvido com HTML, JavaScript e CCS. 
O FRONTEND interage com duas API's externas públicas que são: "ViaCEP" em que o usuário vai inserir o CEP dele e vai ter um retorno de todos os dados do endereço com base naquele CEP e ele vai saber quantos carregadores tem no bairro dele, na cidade dele e no estado dele. A segunda API é a "SheetJS", na qual o usuário com um clique no botão vai poder fazer baixar a lista de carregadores em uma planilha Excel.

Outro componente da arquitetura da aplicação consiste na interação do BACKEND com o FRONTEND, em que foi desenvolvida uma API REST, com documentação em SWAGGER e o banco de dados em SQLite.


Abaixo temos mais detalhes sobre como utilizar o projeto apresentado:




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

