from CpfCnpj import CpfCnpj

cpf = 12345678909  #por entre aspas para ser string e não ser considerado numero
"""
cpf = str(cpf) #converte pra string, pois len() só aceita string
tamanho_cpf = len(cpf)
print(tamanho_cpf)
#instanciar classe Cpf criado na mão
obj_cpf = Cpf(cpf)
print(obj_cpf)

"""

#cpf = Cpf('01234567890')
cpf = CpfCnpj('12354367996','cpf')

#classe abaixo recebe string como parametro
print(cpf)   #retorna true or false

cnpj = CpfCnpj('22981234000108','cnpj')
print(cnpj)

