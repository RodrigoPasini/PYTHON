'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
total=totmil=menor=cont=barato=0
print("{:-^40}".format(" LOJA SUPER BARATÃO "))
while True:
    produto=str(input("Nome do produto? "))
    preco=float(input("Preço: R$ "))
    cont+=1
    total+=preco
    if preco>1000:
        totmil+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=produto
    resp= " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}".format(" FIM DO PROGRAMA "))
print(f"Total de gastos com a compra é de R$ {total:.2f}.")
print(f"A quantidade de produtos que custam mais de R$ 1.000,00 é de {totmil}.")
print(f"O nome do produto mais barato é {barato}. E ele custa R$ {menor:.2f}.")
