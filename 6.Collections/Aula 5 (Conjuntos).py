"""
Um conjunto em python é representado por vários elementos e não possui valores repetidos.
Ela  não possui um indice ou seja eu não posso acessar o conjunto de forma aleatoria igual a uma lista
mas ainda é possivel interar sobre elas com um for, mas a ordem não é a mesma ordem da entrada
ele pode ser chamado de forma literal com o {} ou pelo seu construtor set()
"""
usuarios_data_science = set([11,23,51,65])
usuarios_machine_learning = {11,52,64,23}

print(usuarios_data_science,usuarios_machine_learning)
#Interagindo pelo conjunto

for valor in (usuarios_data_science | usuarios_machine_learning):
    print(valor)
# como o tipo de dado é conjunto ela possui a união do conjunto ou seja A U B tem uma representação

print(usuarios_machine_learning | usuarios_data_science)

#Operação de interserção  A /\ B
print(usuarios_machine_learning & usuarios_data_science)

# A - B
print(usuarios_data_science - usuarios_machine_learning)

#A ou esclusivo B
print(usuarios_data_science ^usuarios_machine_learning)

#como os conjuntos são interaveis você consegue utilizar os metodos dos interaveis como in for ...