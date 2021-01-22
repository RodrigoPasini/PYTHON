#Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont=("zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove", "dez",
        "onze", "doze", "treze", "quatorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
        while True:
                núm = int(input("Digite um número entre 0 e 20: "))
                if 0<= núm <=20:
                        break
                print("Tente novamente. ", end="")
        print(f"Você digitou o número {cont[núm]}.")
        fim=""
        while fim not in ["S", "N"]:
                fim = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if fim =="N":
                break


