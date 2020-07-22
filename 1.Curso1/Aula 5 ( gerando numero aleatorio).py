#para "criar" um número pseudo-aleatório a gente utiliza a biblioteca random
#para utiliza-lá é necessário exportar ela
# para saber quais bibliotecas já estão presentes no python vc deve entrar no builtin do python no google

import random #importando random
numeroAleatorio = random.random() * 100# vai gerar um número aleatório entre 0.0 e 1.0
#print(numeroAleatorio)
#round arredonda o valor
#print(round(numeroAleatorio))
# tem tb o random.uniform(y,z) que gera um float y<= x <= z
# e o random.randrange(X) de 0 até x-1 ou (x,y) de x até y-1 , ou (x,y,z) de x até y , pulando de z em z
print(random.randrange(10))
print(random.randrange(0,10))
print(random.randrange(0,10,2))
# temos o abs para deixar o numero em módulo
abs(-10)