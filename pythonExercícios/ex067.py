#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n=int(input("Escolha a tabuada que deseja realizar: "))
    print("-"*40)
    if n<0:
        break
    for s in range(0,11):
        m = n * s
        print(f"{n} X {s} = {m}")
        s += 1
    print("-" * 40)
print("CÁLCULO ENCERRADO")
