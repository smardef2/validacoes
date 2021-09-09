from CpfCnpj import Documento
from TelefonesBr import TelefonesBr
from cdatasBr import DatasBr
from c_acesso_cep import Busca_Endereco

scpf = "01234567890"
scnpj = "57868643000179"
obj = Documento.cria_docto(scnpj)
print(obj)

telefone = "1112349999"
objTel = TelefonesBr(telefone)
print(f'Telefone {telefone} formatado: {objTel}')

obj = DatasBr()
print(f'Mês do cadastro: {obj.mes_cadastro()}')
print(f'Dia da semana do cadastro: {obj.dia_semana()}')
print(f'Imprimindo o obj data: {obj}')
print(f'Tempo de cadastro do cliente: {obj.tempo_cadastro()}')

cep = '01001000'
obj_cep = Busca_Endereco(cep)
print("Cep: {}".format(obj_cep))
bairro, localidade, uf = obj_cep.acessa_via_cep()
print("bairro {},localidade {}, uf {}".format(bairro,localidade, uf))