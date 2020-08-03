"""Dicionarios no python
Um dicionario é um tipo de estrutura de dado que armazena um conjuto de elementos de chave e valor
cada elemento possui um indentificador (chave) e seu valor ele pode ser criando de forma
literal ou pelo seu contrutor
"""

dicionario1 = {"blue":"azul","red":"vermelho"} #forma mais utilizada
dicionario2 = dict(blue = "azul" ,red = "vermelho" )

#podemos pegar um valor do dicionario com o get e caso a chave não exista retornar algum valor

print(dicionario1.get("Yellow",0))
print((dicionario1.get("blue",0)))

#podemos modificar um valor no dicionario

dicionario1["blue"] = 2
print(dicionario1)

#Podemos adicionar um valor novo

dicionario1["green"] = "verde"
print(dicionario1)

#Podemos remover um valor do dicionário

del dicionario1["blue"]
print(dicionario1)

#podemos verificar se existe uma chave no dicionario

print("white" in dicionario1)

#Podemos interar sobre o dicionario , mas ele retornará as chaves e não os valores

for chave in dicionario1:
    print(chave)

#outra forma melhor

for chave in dicionario1.keys():
    print(chave)

#para interar pelos valores

for valor in dicionario1.values():
    print(valor)

#pegando as duplas, irá retornar uma tupla

for chave,valor in dicionario1.items():
    print(chave,valor)

#Podemos criar um valor padrão para o dicionario, ou seja quando eu chamar uma chave que não existe ela me retorna um padrão
#Fazemos isso com o defaultdict da biblioteca colletions

from  collections import defaultdict

dicionario_padrao = defaultdict(int) #O parametro é uma função ou um valor no caso passado é o int() que retorna 0

print(dicionario_padrao["teste"]) #Como não existe a chave teste ele retornará 0

"""Exemplo de uso de um dicionario
Pense em uma situação em que você recebe um texto qualquer e você quer saber quais palavras aparecem naquele texto
e quantas vezes ela se repete
"""

texto_exemplo = "Texto é um conjunto de palavras e frases encadeadas que permitem interpretação e transmitem uma " \
                "mensagem. É qualquer obra escrita em versão original e que constitui um livro ou um documento escrito." \
                " Um texto é uma unidade linguística de extensão superior à frase.".lower()

dicionario_exemplo = defaultdict(int)

for palavra in texto_exemplo.split():
    #caso não encontre o valor retornará 0
    dicionario_exemplo[palavra] +=1

print(dicionario_exemplo)

#Podemos melhorar usando o contador do python que aceita um interavel como apramero e ja conta
from collections import Counter
dicionario_exemplo = Counter(texto_exemplo.split())
print(dicionario_exemplo)

#o defaultdict não recebe exclusivamente um int ela trabalha com qualquer tipo passado

class Conta:
    def __init__(self):
        print("Criando conta")

dicionario_exemplo2 = defaultdict(Conta)
dicionario_exemplo2["ContaJoão"]



