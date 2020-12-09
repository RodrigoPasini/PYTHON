#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s=0
cont=0
for n in range(1,501,2):
    if n%3==0 and n%2==1:
        cont=cont+1
        s=n+s
        print(n, end=", ")
print("\nA soma dos {} valores solicitados é {}.".format(cont, s))
print("FIM")