#a expressão regular em python é dada pela biblioteca re
import re
padrão = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
#melhorando o padrão , para encontrar caracteres esspeciais que pode ajudar na ER pesquisar na documentação do re
# eu posso colocar o alcance do caracter com um "-" por ex [a-z] irá procurar todos os caracteres menusculos entre a-z no texto
#tembem posso dizer a quantidade de vezes que ela ira aparecer com o {quantidade}
#posso tambem quantificar o intervalo ex [0-9]{4,5} encontra numeros de 0 a 9 com 4 ou 5 caracteres tipo 0000 99999 15978 etc
padraoMelhorado = "[0-9]{4,5}[-]*[0-9]{4}"# esse * é o mesmo da cadeira de teoria da computação
#significa que ele encontrara  o numero com ou sem o -
email1 = "iasjdiajsdia 91435-1234asdijiajdia 12303214 asidj masdi6487-1232 qjeqj asdkaodss"
email2 = "Um email1230-3214 qualquer6487-1232 totalmente aleatorio com um numero aqui 91435-1234"
email3 = "asd91435-1234 jasipjad 6487-1232 asud 1230-32149 u12 129381=12390123= 1238781123812 "

#Usando o metodo re.search podemos pesquisar os padrões de um texto onde eu passo o padrão e o texto que quero analisar
#porem o search encontra apenas o primeiro, para buscar todos os matchs vc tem que usar o findall que retornara uma lista
retorno1 = re.search(padraoMelhorado,email1)
list1 = re.findall(padraoMelhorado,email1)
retorno2 = re.search(padraoMelhorado,email2)
list2 = re.findall(padraoMelhorado,email2)
retorno3 = re.search(padraoMelhorado,email3)
list3 = re.findall(padraoMelhorado,email3)


print(retorno1.group())
print(retorno2.group())
print(retorno3.group())
print(list1)
print(list2)
print(list3)