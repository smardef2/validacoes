# incluindo comentario
import requests
# testando
class Busca_Endereco:
    def __init__(self,cep):
        cep = str(cep)  #converte para string para ter certeza que é string
        if self.cep_eh_valido(cep):
            self._cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def cep_eh_valido(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return '{}-{}'.format(self._cep[:5],self._cep[5:])  #cep de 0 a 5 (5 não incluso), depois , cep de posição 5 em diante

    #retorno para cep '01001000'
    """
    {
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "complemento": "lado ímpar",
  "bairro": "Sé",
  "localidade": "São Paulo",
  "uf": "SP",
  "ibge": "3550308",
  "gia": "1004",
  "ddd": "11",
  "siafi": "7107"
}
    """
    def acessa_via_cep(self):    #teste em teste2.py
        url = "https://viacep.com.br/ws/{}/json/".format(self._cep)
        r = requests.get(url)
        dados = r.json()
        return (dados["bairro"], dados["localidade"],dados["uf"])