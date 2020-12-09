#Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.
n1=int(input("O primeiro valor é = "))
n2=int(input("O segundo valor é = "))
soma=n1+n2
print("A soma entre {} e {} é = \033[2;31;43m{}\033[m.".format(n1,n2,soma))