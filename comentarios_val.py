"""
No Pycharm, nos funções de import, segure o 'ctrl' e aponte com o mouse em cima da bilbioteca de datetime que vc irá o codigo da função da biblioteca

no google procure por: valicao cpf
 tem algoritmo para validar cpf

- tem pacotes prontos para reutilizar metodo de pcte de classe externa
- procure no google por  'pypi'
  site: pypi - the python package index - pypi
  entra no site e em procurar coloque: "valida cpf"
  e acha pacotes pra validar cpf, ve nos detalhes:
   validate-docbr 1.2.0   #pip use na pasta do projeto, é por projeto que se instala os pacotes adicionais e não no python como um todo
    pip install validate-docbr

   No lado esquerdo do site, menu, tem Project libs , se clica vai pro github ver codigo fonte
   todo cod fonte do pacotes estão lá

- no pycharm, no terminal instale com o comando pip acima

- padrão de projeto factory
  Criou classe Documento q decide se instancia classe CPF ou CNPJ
  o padrão de projeto Factory pode ser bastante útil em situações em que temos objetos que pertencem a classes semelhantes.
  É importante perceber que os métodos das subclasses da classe factory possuem os métodos com os nomes iguais! Dessa forma, podemos usar a factory sem se preocupar em qual classe foi instanciada.
  - construímos uma factory que decidia entre instanciar uma classe responsável por CPFs e outra por CNPJs. Uma das vantagens de usar esse padrão de projeto é facilitar o crescimento do código.
    - as alterações necessárias, no caso de inserirmos um documento novo é
     - A nova classe precisará ter todos os métodos com os mesmos nomes das outras classes filhas.
      Para conseguirmos usar qualquer instância retornada pelo Factory livremente, os métodos das classes filhas precisam ser iguais.

#--------------------------------
expressoes regulares
 As expressões regulares servem para encontrar padrões bem definidos dentro de uma cadeia de caracteres em um texto ou str maiores. Por exemplo, se temos um e-mail com um volume textual enorme contendo um número de telefone específico, poderemos extraí-lo sem precisarmos ler todo o conteúdo.
 conhecer os caracteres especiais da linguagem e metodos para usar exp regular

- Os colchetes [] são caracteres especiais que definem um range ou um grupo de caracteres, como [0-9], [a-z] ou [abc] por exemplo;
- Já o * pega uma ou mais ocorrências do padrão definido anteriormente;
- As chaves {} nos permitem definir uma quantidade específica de vezes que queremos que o padrão se repita ou um intervalo de
   possibilidades, como [abc]{5} por exemplo;
- O \w pode ser qualquer número de zero a nove ou letra de "A" a "Z";
- \d - qqr numero de 0 a 9
- A barra | representa uma coisa ou outra como em @|$ por exemplo;
- Os parênteses () capturam um grupo, e veremos sua importância mais adiante.

[abc] - pega ou a, ou b, ou c
[a-z] - pega de a a z

import re   #biblioteca de expressões regulares

--------------
#criar mascara com telefone direito
() captura e agrupa, separa o padrao em grupos
padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
#qdo usa parenteses agrupa - vantagens:
  - se usa findall a resposta vem toda separada por grupo: pais, cod area, primeira parte tel, segunda parte telefone
  - se usa search, qdo usa resposta.group() pode por o indice que quer a resposta pq ai pega 1, cod pais, 2 cod area e etc

#qdo agrupa tb pode usar o"?" que indica que o grupo pode ou não existir
  # cuidado: qdo omite codigo do pais, se procura no group(1) dá none, pois não teve cod do pais, se procura group(2) devolve cod area e o resto ok

Nota: capturar em grupo utilizando os parênteses () é importante, pois deixa o padrão melhor explicado e mais fácil de ser controlado, além de os grupos poderem ser separados utilizando o método .group(index)

Ex: Analise os e-mails abaixo:
email_um = rodrigo@gmail.com
email_dois = rodrigao1993@4shared.org.uk
email_tres = rodrigo@rodrigo.br
email_quatro = rodrigo123@python.py.br
 Um padrão que serviria para capturar todos os e-mails acima seria:
\w{2,50}@\w{2,15}\.[a-z]{2,3}\.?([a-z]{2,3})?

#-------------------------------------------------------------
DATETIME
Em sua biblioteca datetime e a classe datetime, o Python possui o método strftime() que receberá a data e a formatação regida por outros caracteres especiais. É bastante parecido com o que fizemos usando as expressões regulares ou regex.
strftime - para formatar datas
%A retorna os dias da semana por extenso, como Sunday;
%d exibe os dias do mês com números de 01 a 31;
%m retorna meses em números de 01 a 12;
%y mostra o ano com apenas dois dígitos;
%Y apresenta o ano em formato de quatro números;
%H retorna o horário no formato decimal, como 00, 001 e etc;
%M exibe os minutos de forma decimal; 01,02,03...
%S apresenta os segundos em decimal.  00,01,02,...

#para somar dias, horas a uma data, use timedelta

#para somar ou subtrair datas, vai direto pq classe datetime já implementou métodos especiais como add e sub para que se possa trabalhar com datas como operações aritméticas
  subtração entre objetos data retorna qtde de dias e minutos entre uma data e outra (mas deve tb retornar anos se houver de diferença?)

-----------------------------
API
  os clientes acessam essa API enviando uma requisição http, seja get() para pegar informação, post() para criar, put() para atualizar algo que já existe ou delete() para deletar.
  A partir disso, a API acessa o sistema ou banco de dados e faz uma ação que retorna uma resposta. Se somente for encontrar uma resposta, o retorno será uma resposta serializada.

  - para encontrar uma api para pesq endereço pelo cep, procure no google
 - no google procure por api cep
    tem viacep que é ibge cep
 - para acessar uma api, existe uma biblioeca do python
 - no google procure por 'requests python' - vem na distribuição do python - não precisa instalar
      https:;;2.pytohon-requests.org ou https://3.python-requests.org/ explica como usar


import requests  #diz que não precisa de pip, ja no python, mas instalei do pycharm clicando em instal qdo marcava erro, pois não reconheceu antes
r = requests.get('https://viacep.com.br/ws/012345678/json/')
print(r)   #devolve response 200 que deu ok
print(r.text)  #devolve o conteudo
print(type(r.text))  #conteudo é do tipo str
#dicionario é como lista,mas para acessar itens ao inves de indices tem chaves nomeáveis
print(type(r.json())) #retorna um dict, dicionario
print(r.json()['cep'])   #obtem só o valor do cep do dicionario


#Via cep
  https://viacep.com.br/ws/01001000/json/   #url para chamar põe cep como parametro e o tipo de resposta que quer obter: json, xml, etc

-------
dir(objeto)   #retorna todos atributos e métodos que objeto possui

- tem muitas apis publicas que se pode usar
 como twiter q pode publicar coisas com twiter, só ver a documentação

"""