# Aqui será testada toda a lógica antes de mandar para classe , e tb testar a a classe
from Cpf_Cnpj import Documento
from TelefonesBr import TelefonesBr
from datas_br import DatasBr
from acesso_cep import Cep

from validate_docbr import CPF # Biblioteca que valida alguns documentos brasileiros
cpf = "01234567890"

objeto_cpf = Documento.cria_documento(cpf)
print(objeto_cpf)
cnpj = "35379838000112"
objeto_cnpj = Documento.cria_documento(cnpj)
print(objeto_cnpj)

telefone1 = "81998116756"
telefone2 = "558199811-6756"

telefone = TelefonesBr(telefone1)

print(telefone)

cadastro = DatasBr()
print(cadastro)
cep = "13041730"
objeto_cep = Cep(cep)

bairro,cidade,uf = objeto_cep.busca_via_cep()
print(bairro,cidade,uf)
