'''cont=1
while cont<=10:
    print(cont, "-> ", end="")
    cont+=1
print("ACABOU")'''
''''n= s = 0
while n!=999: # 999 é como se fosse uma FLAG (ponto de parada)
    n=int(input("Digite um numero: "))
    s+=n
print("A soma dos númeors digitados vale {}.".format(s))'''
n = s = 0
while True:
    n=int(input("Digite um número: "))
    if n==999:
        break
    s+=n
#print("A soma dos valores digitados é de {}".format(s))
print(f"A soma dos valores digitados é de {s}")