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
#numero = ""
print(ehStringValida(String))
#print(ehStringValida(numero))
# # replace
# string.replace(x,y,z) o replace troca na string o passada os valores de x por y , e o z é a quantidade de vezes
#que ele ira fazer essa troca , caso seja vazio todos os valores de x são trocados por Y
stringex = "joao lucas menezes paulino da paes paes paes"
print(stringex.replace("paes", ""))
print(stringex.replace("paes","",2))
#metodos upper() deixa maiusculo e lower() deixa minuscula
#startswith() verifica se o parametro passado começa na string dada e retorna true ou false