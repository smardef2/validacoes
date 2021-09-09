from validate_docbr import CPF
from validate_docbr import CNPJ

class Documento:
    @staticmethod
    def cria_docto(docto):
        if len(docto) == 11:
           return DocCpf(docto)
        elif len(docto) == 14:
            return DocCnpj(docto)
        else:
            raise ValueError('Qtde de digitos incorreta!')


class DocCpf:
    def __init__(self,docto):
        if self.valida(docto):
            self.cpf = docto
        else:
            raise ValueError("Docto inválido!")

    def __str__(self):
        return self.format()

    def valida(self, docto):
        validador = CPF()
        return validador.validate(docto)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self,docto):
        if self.valida(docto):
            self.cnpj = docto
        else:
            raise ValueError("Cnpj inválido!")

    def __str__(self):
        return self.format()

    def valida(self,cnpj):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(cnpj)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

