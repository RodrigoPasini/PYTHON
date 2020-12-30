'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
tot18 = totH = totM20 = 0
while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    idade=int(input("IDADE: "))
    sexo= " "
    while sexo not in "MF":
        sexo = str(input("Informe SEXO: [M/F] ")).strip().upper()[0]
    if sexo=="M":
        totH+=1
    if idade>18:
        tot18+=1
    if sexo=="F" and idade<20:
        totM20+=1
    pergunta= " "
    while pergunta not in "SN":
        pergunta = str(input("Deseja cadastrar uma nova pessoa? [S/N]")).strip().upper()[0]
    if pergunta == "N":
        print("Cadastros encerrados!")
        break
print(f"Há {tot18} pessoas com mais de 18 anos.", end=" ")
print(f"Foram cadastrados {totH} homens.", end=" ")
print(f"Há {totM20} mulheres com menos de 20 anos.")
