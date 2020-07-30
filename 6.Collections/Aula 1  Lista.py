#lista

#Lista no python é dada pelo []
lista = [0,1,2,3]
print(lista)
print(type(lista))
#Eu posso pegar os valores da lista de qualquer posição basta passar o seu indice
print(lista[2])
#Ela possui alguns métodos como o len que retorna o tamanho da lista
print(len(lista))
#Outro método é o append que adiciona um valor no final da lista
lista.append(2)
print(lista)
#Na lista posso percorrer todos os elementos dela com o for
for item in lista:
    print(item)
#Além disso eu posso remover um valor dentro da lista com o metodo remove, mas só remove o primeiro
lista.remove(2)
print(lista)
#Para limpar a lista existe o método clear
lista.clear()
#Podemos verificar se algo está dentro da lista e retornará true ou false
lista = [0,1,2,3]
print(2 in lista)
#Podemos adicionar em alguma posição especifica , sendo 0 o primeiro elemento
lista.insert(0,4)
#Posso colocar varios elementos atravez do extend, onde eu passo uma lista e ele adiciona cada elemento isoladamente na minha lista
lista.extend([6,8,7,9])
print(lista)
#Criando uma nova lista a partir de uma existente, porem fazendo uma operação nela
lista2 = [(valor+1) for valor in lista]
print(lista2)
#Posso colocar uma condição para filtrar os valores
lista2 = [(valor) for valor in lista if valor > 5]
print(lista2)
#Além disso pode-se fazer transformações passando uma função
def soma1(valor):
    return valor+1

lista2 = [soma1(valor)for valor in lista if valor > 5]
#Não está relacionado a lista mas eu posso criar uma função que recebe um parametro e caso não seja passada ,
#posso colocar um valor padrão
#def soma(a =0 , b = 0):  coloquei os valores padrões de a =0 e b = 0 caso não receba esses parametros
#   return a+b

#Boas praticas de lista, caso queira passar uma lista como um parametro de uma função e criar um padrão
#Sempre criar o padrão como None e fazer um if dentro da função para verificar se é none
def faz_processamento_de_visualização(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    lista.append(13) # previne de criar uma lista e adicionar 13 nela . Neste caso