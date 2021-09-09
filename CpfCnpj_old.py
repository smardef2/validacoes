from validate_docbr import CPF
from validate_docbr import CNPJ

class CpfCnpj:
    def __init__(self, documento,tipo_docto):
        documento = str(documento)
        self.tipo_docto = tipo_docto
        if(self.tipo_docto == 'cpf'):
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF invalido!')
        elif(self.tipo_docto == 'cnpj'):
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ inválido')
        else:
            raise ValueError('Documento invalido')

    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida!')

    def cnpj_e_valido(self,cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError('Qtde de digitos invalida')


    def __str__(self):
        if self.tipo_docto == 'cpf':
            return self.format_cpf()
        else:
            return self.cnpj

    # devolve mascara
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    # dividir cpf em pedaços
    def format_cpf2(self):
        fatia1 = self.cpf[:3]  # fatia string de 0 a 3
        fatia2 = self.cpf[3:6]
        fatia3 = self.cpf[6:9]
        fatia4 = self.cpf[9:]
        return "{}.{}.{}-{}".format(
            fatia1, fatia2, fatia3, fatia4)
