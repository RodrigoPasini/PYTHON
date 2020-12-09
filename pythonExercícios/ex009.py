#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n=int(input("Informe o número da tabuada que deseja realizar: "))
print("Tabuada do número {}".format(n))
i=0
while i<=10:
    print(n,"X", i, "=", n*i)
    i = i+1