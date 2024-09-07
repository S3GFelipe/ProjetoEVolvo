Instruções de uso do Front-End do MVP3 do aluno Felipe Florêncio de Andrade

Para visualizar o front, basta fazer o download de todos os arquivos presente no diretório do Git Hub e abrir o arquivo "index.html", dessa forma já é possível visualizar toda a construção do front-end.


A parte complementar do projeto referente ao Back-End esta presente no outro diretório do Git Hub: https://github.com/S3GFelipe/MVP3-Back.git



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
