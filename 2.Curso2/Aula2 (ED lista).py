# A lista em python e dada com o []
lista = [1,2,4,3,5,0]
lista2 = ["a","d","b","c"]
print(type(lista))
#Algumas operações pesquisar built in para mais functions
# x in lista  verifica se x existe em lista como uma string tb é uma sequencia tb funciona
print("x" in lista)
palavra ="salve"
print("a" in palavra)
#min() valor minimo da lista
print(min(lista))
print(min(lista2))
#max() valor maximo da lista
print(max(lista))
print(max(lista2))
#len() tamanho da lista
print(len(lista))
#append(x) adiciona x ao final da lista
lista.append(4)
print(lista)
#remove(x) remove o primeiro x da lista
lista.remove(4)
print(lista)
#pop([i]) retorna e remove o valor na posição i
print(lista.pop(1))
print(lista)
#insert(i,x) coloca i na posição x da lista
lista.insert(2,0)
print(lista)
#reverse() inverte a lista
lista.reverse()
print(lista)
#clear() limpa a lista
lista.clear()
print(lista)
#usando for dentro da lista MASSA DE MAIS
lista2= ["-" for i in range(0,6)]
print(lista2)

