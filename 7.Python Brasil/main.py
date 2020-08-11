# Aqui será testada toda a lógica antes de mandar para classe , e tb testar a a classe
from Cpf import Cpf
from validate_docbr import CPF # Biblioteca que valida alguns documentos brasileiros
cpf = "01234567890"

objeto_cpf = Cpf(cpf)
print(objeto_cpf)

cpf2 = CPF()

print(cpf2.validate(cpf))