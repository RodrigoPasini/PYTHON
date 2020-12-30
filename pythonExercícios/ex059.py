'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1=int(input("Primeiro valor: "))
n2=int(input("Segundo valor: "))
opcao=0
while opcao != 5:
    print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa")
    opcao=int(input(">>>>> Qual é a sua opção?"))
    if opcao == 1:
        soma=n1+n2
        print("A soma entre {} e {} é = {}". format(n1,n2,soma))
    elif opcao == 2:
        mult=n1*n2
        print("A multiplicação entre {} e {} é = {}". format(n1, n2, mult))
    elif opcao == 3:
        maior=0
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print("Entre {} e {} o maior valor é {}.".format(n1,n2,maior))
    elif opcao == 4:
        print("Informe os números novamente.")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao==5:
        print("Finalizando...")
        sleep(2)
    else:
        print("Opção inválida. Tente novamente.")
    print("=-="*10)
print("Fim do programa! Volte sempre.")
