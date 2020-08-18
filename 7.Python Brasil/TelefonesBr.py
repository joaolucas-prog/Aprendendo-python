import re
class TelefonesBr:

    def __init__(self,telefone):
        if self.valida(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número inválido!")

    def valida(self,telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta =  re.findall(padrao,telefone)
        if resposta:
            return True
        else:
            return False

    def __str__(self):
        return self.formata()

    def formata(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        grupos = re.search(padrao,self.numero)
        if grupos.group(1) == None:
            codigo_pais = "55"
        else:
            codigo_pais = grupos.group(1)
        codigo_estado = grupos.group(2)
        numero_parte1 =grupos.group(3)
        numero_parte2 = grupos.group(4)

        return f"+{codigo_pais}({codigo_estado}){numero_parte1}-{numero_parte2}"