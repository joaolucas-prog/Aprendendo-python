#no python None é equivalente ao Null
string = None
#lembre-se que None é diferente de vazia
stringVazia = ""
#CURIOSIDADE podemos utilizar o raise para mostrar algo para o usurio

def ehStringValida(string):
    if string:
        print(string)
    else:
        raise LookupError("testando")

String = "string"
numero = ""
print(ehStringValida(String))
print(ehStringValida(numero))

