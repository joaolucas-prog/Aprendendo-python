#Problematização
"""
Imagine uma situação em que eu estou criando uma lista de objetos, e por algum motivo eu passei
esse objeto na lista em 2 posições diferentes mas na mesma lista exemplo
lista = [Objt1 , Objt2 , Objt1]
Ao fazer isso vc corre o risco de alguem mexer em algum dos objetos repetidos e modificar ambos,pois
o objeto não foi instanceado então ambos apontam para a mesma referência e caso vc altere um
todos os locais em que aquele objeto é referenciado ele tem seu valor alterado.
"""
"""
Situação 2 , Eu quero criar uma lista imutavel , onde cada elemento daquela lista tem um significado
EX:
Quero criar uma lista onde a primeira posição indica nome e a segunda indica idade, mas uma vez criada
eu não posso alterar aquele valor. 
Para isso eu utilizo as tuplas
"""
joao = ( 'joao' , 21)
"""
A ordem de significado da tupla deve ser respeitada, se eu trabalho com tupla e quero que na posição 1
seja o nome e na posição 2 seja a idade eu tenho que respeitar essa ordem na hora de criar outras tuplas

Resumo usar tuplas estará te levando a um estilo de programação funcional
Enquanto usar listas estará levando a um estilo orientado a objetos

Mas nada impede de vc utilizar ambos os objetos tanto junto como isolados dependendo da sua ideia
e da utilidade , se utilizar tupla em um mundo OO faz sentido em tal situação , é totalmente valido usar
da mesma forma o contrário
"""