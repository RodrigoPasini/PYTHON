#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista=[]
par=[]
impar=[]
while True:
    lista.append(int(input("Digite um número: ")))
    r=""
    while r not in ["S", "N"]:
        r=str(input("Deseja continuar? [S/N]")).upper()[0]
    if r in "Nn":
        break
for i, v in enumerate(lista):
    if v%2==0:
        par.append(v)
    elif v%2 ==1:
        impar.append(v)
print("-="*30)
print(f"A lista dos números digitados é: {lista}")
print(f"A lista de números pares é: {par}")
print(f"A lista de números ímpares é: {impar}")