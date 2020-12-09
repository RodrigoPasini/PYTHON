#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
totmaior=0
totmenor=0
for c in range(1,8):
    anonasc=int(input("Em que ano a {} pessoa nasceu? ".format(c)))
    idade = date.today().year - anonasc
    cont=c
    if idade<18:
        totmenor+=1
    else:
        totmaior+=1
print("Ao todo tivemos {} pessoas maiores de idade.".format(totmaior))
print("E também tivemos {} pessoas menores de idade.".format(totmenor))
