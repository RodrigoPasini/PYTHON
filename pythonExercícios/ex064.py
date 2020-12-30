#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n=0
a=1
s=0
while n!=999:
    n=int(input("Digite um número [999 para PARAR]: "))
    a+=1
    b=a-1
    s=s+n
    t=s-999
print("Foram digitados {} números e a soma deles é igual a {}.".format(b,t))