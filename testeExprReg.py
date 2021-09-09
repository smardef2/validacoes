import re
import requests   #api

#biblioteca de expressões regulares
padrao = "[0-9][a-z][0-9]"  #define ache um numero de 0 a 9, depois uma letra e depois um numero
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao,texto)
print(f'resposta pura: {resposta}')   #devolve se match, span=(4,7) indica em q posição achou o padrão e match=, o que encontrou
print(f'resposta.group: {resposta.group()}')   #agora só devolve a string que obedece o padrão

#padrão pegar 1 letras
padrao = "[0-9][a-z]{1}[0-9]"  #define ache um numero de 0 a 9, depois 2 letras e depois um numero
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao,texto)
print(f'procurando numero,letra,numero em "{texto}": `{resposta.group()}')   #da erro pq não deu match

#padrao para encontrar emails
#nome@dominio.com.br
#padrão abaixo define letras ou numeros de 5 a 50 repetições,depois um '@' depois letras ou numeros
  # repetindo de 3 a 10 vezes, depois vem um '.' depois letras ou numeros que se repetem de 2 a 3 vezes depois outro ponto e depois mais 2 a 3 letras ou numeros
padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbccc rodrigo123@gmail.com.br lixo"
resposta = re.search(padrao,texto)
print(resposta.group())   #obteve somente 'rodrigo123@gmail.com.br' ignorando texto antes e depois

#agoraa muda pra ser só Brasil e só letras pra dominio
padrao = "\w{5,50}@[a-z]{3,10}.com.br"
texto = "aaabbbccc rodrigo123@gmail.com.br lixo"
resposta = re.search(padrao,texto)
print(resposta.group())   #obteve somente o email

#procurar por num de telefone
#(xx)9999-9999
padrao= "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto 21224561289 e do num 1112349999"
resposta = re.findall(padrao,texto)  #encontra todas correspondencias de um padraõ em um texto
print(f'Telefones: {resposta}') #devolve lista com todas ocorrencias do texto

cep = '01001000'
url = "https://viacep.com.br/ws/{}/json/".format(cep)
r = requests.get(url)
print(r.text)