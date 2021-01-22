'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
numeros=[]
s=0
while True:
    n=int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        s+=1
    r=""
    while r not in ["S", "N"]:
        r=str(input("Deseja continuar? [S/N]")).upper()[0]
    if r in "Nn":
        break
print("-="*30)
print(f"Você digitou {s} elementos.")
numeros.sort(reverse=True)
print(f"A lista dos números digitados foi: {numeros}")
if 5 in numeros:
    print("O Valor 5 faz parte da lista.")
else:
    print("O valor 5 não faz parte da lista.")