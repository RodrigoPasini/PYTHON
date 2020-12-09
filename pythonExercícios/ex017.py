#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co=float(input("Informe o valor do cateto oposto: "))
ca=float(input("Informe o valor do cateto adjacente: "))
print("O valor do cateto oposto é {}.\nJáo valor do cateto adjacente é de {}.\nO cálculo da hipotenusa é de {:.2f}.".format(co,ca,hypot(co,ca)))


