# Aqui será testada toda a lógica antes de mandar para classe , e tb testar a a classe
from Cpf_Cnpj import Documento
from validate_docbr import CPF # Biblioteca que valida alguns documentos brasileiros
cpf = "01234567890"

objeto_cpf = Documento.cria_documento(cpf)
print(objeto_cpf)
cnpj = "35379838000112"
objeto_cnpj = Documento.cria_documento(cnpj)
print(objeto_cnpj)
