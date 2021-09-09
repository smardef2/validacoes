import re

#telefone pode ter indicação do pais, alguns paises identifica com 2 digitos e outros com 3
#55 11 91234-9999   - telefone fixo 4 digitos na primeira parte e celular tem 5
class TelefonesBr:
    def __init__(self,telefone):
        self._padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"  #num pais opcional, cod area, 4 a 5 digitos primeira parte tel, segunda parte tel
        if self.valida_telefone(telefone):
            self._numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self,telefone):
        resposta = re.findall(self._padrao,telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        resposta = re.search(self._padrao, self._numero)
        numero_formatado = "+{} ({}) {}-{}".format(
            resposta.group(1), resposta.group(2),resposta.group(3),resposta.group(4)
        )
        return numero_formatado
