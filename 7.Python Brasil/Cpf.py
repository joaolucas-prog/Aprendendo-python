class Cpf:

    def __init__(self,documento):
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def cpf_e_valido(self,documento):
        if len(documento) == 11:
            return True
        else:
            return False
    def __str__(self):
        return self.formata_cpf()

    def formata_cpf(self):
        pedaco1 = self.cpf[:3]
        pedaco2 = self.cpf[3:6]
        pedaco3 = self.cpf[6:9]
        pedaco4 = self.cpf[9:]
        return (
            f"{pedaco1}.{pedaco2}.{pedaco3}-{pedaco4}"
        )