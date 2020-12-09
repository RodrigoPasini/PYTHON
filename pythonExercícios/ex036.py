#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa=float(input("Valor da casa: R$ "))
salario=float(input("Salário do comprador: R$ "))
anos=int(input("Quantos anos de financiamento? "))
prestacao=casa/(anos*12)
print("Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}".format(casa,anos,salario))
if prestacao>(salario*0.3):
    print("\033[41mEmprestimo NEGADO!\033[m")
else:
    print("\033[42mEmréstimo AUTORIZADO!\033[m")
