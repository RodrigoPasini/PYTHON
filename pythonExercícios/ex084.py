'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
temp=[]
princ=[]
pesado = leve = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append((int(input("Peso: "))))
    if len(princ)==0:
        pesado=leve=temp[1]
    else:
        if temp[1]>pesado:
            pesado=temp[1]
        if temp[1]<leve:
            leve=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=""
    while resp not in ["S", "N"]:
        resp=str(input("Deseja continuar? [S/N]")).upper()[0]
    if resp in "Nn":
        break
print("-="*30)
print(f"Foram cadastradas {len(princ)} pessoas.")
print(f"O maior peso foi de {pesado}kg. Peso de ", end="")
for p in princ:
    if p[1]==pesado:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso foi de {leve}kg. Peso de ", end="")
for p in princ:
    if p[1]==leve:
        print(f"[{p[0]}] ", end="")
print()
