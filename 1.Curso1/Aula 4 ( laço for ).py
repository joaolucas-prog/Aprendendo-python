#LAÇO FOR

for a in range(4):#começa do zero e vai até 3 o 4 é exclusivo ,seria a quantidade de for
    print(a)
print("--------------")
for b in range(2,4):#começa do 2 e vai até o 3, lembrando o 4 é exclusivo
    print(b)
print("--------------")
for c in range(1,4,2):#começa do 1 vai até 3 mas pula de 2 em 2
    print(c)
print("--------------")
for d in [1,2,3,4,5]:#percorre todo o array
    print(d)
print("--------------")
#para encerrar um laço vc usa o break
#para continuar um laço mesmo com condições anteriores aceitas use continue
#operadores logicos or e and
for i in range(100000):
    print(i)
    if(i == 1 or i == 0):
        print("1 ou 0")
        continue
    if(i > 3 and i == 5):
        break
