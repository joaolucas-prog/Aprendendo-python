#valores booleanos
# ou  = or
# e   = and
# não = not
palavra = "   uma string qualquer   "
#Funções importantes da String: para saber todas pesquisar no built in string
#capitalize() transforma a 1 lentra em Maiuscula e resto menuscula
print(palavra.capitalize())
#endswith("string") se termina com a string passada
print(palavra.endswith("uer"))
#lower() transforma tudo em menusculo
print(palavra.lower())
#upper() transforma tudo e maiusculo
print(palavra.upper())
#strip() retira todos os caracteres passados no parametro do inicio e no final da String
# caso fique "vazio" retira todos os espaços em brancos
print(palavra.strip())
print(palavra.strip('umaquer'))
#replace('a','b') substitui todas as letras 'a' por 'b'
print(palavra.replace('r','l'))
#find(a) verifica se existe a na string e em que posição ela está buscando a primeira letra igual
# , caso contrário retorna -1
print(palavra.find("r"))