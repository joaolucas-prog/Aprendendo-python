"""
if else no python
"""
num1=1
num2=2
if( num2 > num1):
    print("2 é maior")
else:
    print("2 é menor")

"""
input recebe um dado digitado e sempre será uma str
"""
entrada = input("Digite algo :")
print(type(entrada))
"""
para dar um cast de str para int vc usa : int(str)
e para dar um cast de int para str vc usa : str(int)
"""
str1 = "2"
int1 = 2
str2 = int(str1)
int2 = str(int1)

print(type(str1),type(str2),type(int1),type(int2))
"""
existe tb o elif que verifica a proxima condição se o if que veio anteiormente for falso 
"""
numero_exemplo = 3

if(numero_exemplo <= 4):
    print("maior que 4")
elif(numero_exemplo < 4):
    print("menor que 4")

if(numero_exemplo  <= 3):
    print("menor ou igual a 3")
if(numero_exemplo > 2):
    print("maior que 2")
"""
Perceba que no caso do elif como o if anterior foi verdadeiro ele não entrou na segunda verificação , 
mesmo o elif estando "correto" , ja no caso de baixo é verificado os 2
"""
