#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p=float(input("Informe o preço do produto: R$ "))
d=p-(p*(5/100))
print("O preço do produto com desconto de 5% é de R$ {:.2f}.".format(d))
