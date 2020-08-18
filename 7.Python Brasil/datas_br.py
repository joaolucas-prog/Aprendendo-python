from datetime import  datetime, timedelta
class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata()

    def mes_cadastro(self):
        lista_meses = [
            "janeiro","fevereiro","março","abril",
            "maio","junho","julho","agosto",
            "setembro","outubro","novembro","dezembro"
        ]
        numero_mes = self.momento_cadastro.month -1
        print(numero_mes)
        return lista_meses[numero_mes]

    def dia_cadastro(self):
        lista_dias = [
            "segunda","terça","quarta","quinta","sexta","sabado","domingo"
        ]
        numero_dia = self.momento_cadastro.weekday()

        return lista_dias[numero_dia]

    def formata(self):

        return self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
    
    def tempo_cadastro(self):
        return datetime.today() - self.momento_cadastro