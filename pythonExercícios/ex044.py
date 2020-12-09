'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
print("{:=^40}".format(" LOJAS DE COMPRAS "))
preco=float(input("Informe o preço do produto: R$ "))
print('''[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] em 3x ou mais no cartão''')
pagamento=int(input("Informe a forma de pagamento: "))
if pagamento==1:
    print("Você teve R$ {:.2f} de desconto no produto adquirido.\nO valor do produto será de R$ {:.2f}.".format((preco*0.10),preco-(preco*0.10)))
elif pagamento==2:
    print("Você teve R$ {:.2f} de desconto no produto adquirido.\nO valor do produto será de R$ {:.2f}.".format(preco*0.05,preco-(preco*0.05)))
elif pagamento==3:
    print("Sua compra será parcelada em 2x de R$ {:.2f}.\nO valor do produto será de R$ {:.2f}.". format(preco/2, preco))
elif pagamento==4:
    parcelas=int(input("Quantas parcelas?"))
    print("Sua compra será parcelada em {}x de R$ {} COM JUROS.\nO valor do produto será de R$ {:.2f}.".format(parcelas,(preco+(preco*0.20))/parcelas,preco+(preco*0.20)))
else:
    print("\033[41mFORMA DE PAGAMENTO INVÁLIDA!\033[m")
