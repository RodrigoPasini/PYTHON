#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
empregado={}
while True:
    empregado["Nome"]=str(input("Nome: "))
    empregado["Ano de Nascimento"]=int(input("Ano de Nascimento: "))
    empregado["CTPS"]=int(input("No. CTPS: [Digite 0 se não tiver]"))
    empregado["Idade"] = datetime.now().year - empregado["Ano de Nascimento"]
    if empregado["CTPS"]!=0:
        empregado["Ano de Contratação"]=int(input("Informe o ano de contratação: "))
        empregado["Salário"]=float(input("Informe o valor do salário: R$ "))
        empregado["Aposentadoria"]=empregado["Idade"]+((empregado["Ano de Contratação"]+35)-datetime.now().year)
    resp=""
    while resp not in ["S", "N"]:
        resp=str(input("Deseja continuar cadastrando? [S/N]")).upper()[0]
    if resp in "Nn":
        break
    print("-="*30)
for i,v in empregado.items():
    print(f" - {i} tem o valor {v}")
