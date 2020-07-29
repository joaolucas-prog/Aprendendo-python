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