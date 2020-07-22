#Uma string em python é dada a um valor que está entre "" podendo ser ela vazia ou n
sobreMim = "Oi meu nome é João Lucas eu tenho 21 anos"
print(type(sobreMim))

#no python podemos acessar qualquer valor da string utilizando um [] e pegar um caracter especifico

caracter = sobreMim[4]
print(caracter)

#podemos também fatiar um pedaço da string utilizando : dentro do []

ex1 = sobreMim[3:15] # o primeiro numero é inclusivo e o segundo exclusivo
print(ex1)
ex2 = sobreMim[10:]# o python entendo que se não passar nada no segundo é para ir até o final da String
print(ex2)
ex3 = sobreMim[:13]#da mesma forma se n passar nada no primeiro , ele entende que é o indince 0
print(ex3)

#podemos encrontrar a posição de um caracter utilizando o metodo built in do python find
#ele retorna o index do primeiro caracter que foi passado como parâmetro se não encontrar retorna -1
exemplo = "www.exemplo.com/q?argurmentos=valorargumento"
index = exemplo.find("=")
print(exemplo[index+1:])# pegando valor do argumento

# Também posso pegar a string e tranformar em um vetor com o metodo built in split
#onde ele criará um array com um separador que você especificou como parâmentro

vetor = exemplo.split("=")
print(vetor)