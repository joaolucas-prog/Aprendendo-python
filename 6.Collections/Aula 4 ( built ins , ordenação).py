"""
Situação: Se eu estou me deparando com uma lista e eu gostaria de saber o indice e o valor daquela lista
ou seja , quero obter o valor a posição dos elementos dentro da lista
eu poderia usar um for junto com um range

for i in range(len(lista)):
    print(i,lista[i])

mas existe um biblioteca pronta no python que ja me retorna isso que e´a enumerate
 é um gerador lazy , ele só é gerado na meidida do necessario e me retorna uma tupla com o indice e o valor do elemento
"""
lista = [15,12,51,31,82,46,5,1,2,25,12,31]

a = list(enumerate(lista)) #aqui estou forçando ela a gerar todos os elementos
print(a)
for valor in enumerate(lista):
    print(valor) #só é gerado o valor quando chamado

"""
É possivel desempacotar os valores da tupla que é gerado 
"""
for indice,valor in enumerate(lista):
    print( indice,valor)

"""
posso desempacotar tambem se tiver mais que 2 elementos
"""
usuarios = [
    ("joao",21,1999),
    ("ingrid",21,1998)
]
"""
Eu posso criar uma variável para cada elemento , mas se eu quiser usar apenas algum elemento especifico?
eu posso passar um "_" que significa que posso descartar aquele elemento que ele não será usando
mas temos que passar na ordem certa para saber qual posição eu quero utilizar
"""

for nome, _ , _ in usuarios:
    print(nome)

"""
Ordenando os elementos na ordem crescente
"""
print(sorted(lista))
#retornara uma nova lista ordenada, caso vc queira mudificar diretamente na lista
lista.sort()
print(lista)
"""
Ordenando os elementos na ordem decrescente
"""
print(sorted(lista,reverse = True))
#da mesma forma que antes
lista.sort(reverse = True)
print(lista)
"""
invertendo os valores da lista
"""
print(reversed(lista))
"""
Ordenando em uma ordem não natural  das coisas por exemplo ordenar varios objetos, como saber qual criterio de ornação seguir?
Você pode dizer um critério a qual o sorted irá seguir na hora de ordenar
por exemplo eu posso reduzir o meu objeto a um valor que possa ser comparado a atraves de uma função e passar como parametro no
sorted
listaObj.sorted(lista,key=funcao_exemplo)

ou podemos passar um atributo como parametro , caso você queria dar acesso a esse parametro, usando uma biblioteca do python

from operator import attrgetter

listaObj.sorted(lista,key = attrgetter("nome_atributo")

ou da melhor forma que eu acho que é utilizando metodos especiais do python 

__lt__(self,outro):  do ingles less then
    return self.atributoComparacao < self.atributoComaracao  #isso se na sua logica um é maior que o outro por
                                                                um certo atributo
                                                                
E se eu tiver 2 objetos com mesmo valor em um atributo e eu quiser usar outro para determinar qual a ordem deles
por exemplo tenho objetos contas e um objeto é maior que o outro caso o saldo seja maior
mas se o saldo for igual eu quero que o criterio agora seja o seu codigo

podemos fazer pelo attrgeter  passando a ordem das comparações

listaObj.sorted(lista,key=attrgetter("saldo","codigo")

Mas eu quero fazer de forma OO e manter meu encapsulamento então 

eu posso usar no lt e criar condições

class Conta:
//implementação
    def __lt__(self,outro):
        if self.saldo != outro.saldo
            return self.saldo < outro.saldo
            
            
Porem isso só funciona para < se eu quiser um <= eu terei que implementar o __eq__
e importar uma classe chamada  ela define todo o resto apenas com a implementação do lt e do eq

from functools import total_ordering
@total_ordering
class Conta:
    //implementaçao
    def __lt__(self,outro):
        //implementaçao
    def __eq__(self,outro):
        //implementaçao
        
Com isso posso comparar se um objeto é <= a outro 
        """
