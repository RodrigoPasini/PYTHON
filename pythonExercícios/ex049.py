#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num=int(input("Digite um número para ver sua tabuada: "))
for cont in range(0,11):
    print("{} X {:2} = {}".format(num,cont,num*cont))
print("CÁLCULO REALIZADO COM SUCESSO!")