#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
vr=float(input("Informe quantos reais você tem na carteira R$: "))
dolar=vr/5.15
print("A pessoa tem R$ {} na carteira e poderá comprar U$ {:.2f}.".format(vr,dolar))
