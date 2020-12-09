#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input("Digite um número inteiro: "))
dobro = n*2
triplo = n*3
rq = n**(1/2)
print("O dobro do número inteiro é {}.\nO triplo do número inteiro é {}.\nA raiz quadrada do número inteiro é {:.2f}. ".format(dobro, triplo, rq))
