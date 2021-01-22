#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    idade=date.today().year-ano
    if idade<14:
        return f'Você tem {idade} anos. VOTO NEGADO'
    elif 16<=idade<18 or idade>65:
        return f'fVocê tem {idade} anos. VOTO OPCIONAL'
    else:
        return f'Você tem {idade} anos. VOTO OBRIGATÓRIO'


print("-"*30)
anoNascimento=int(input("Ano de nascimento: "))
print(voto(anoNascimento))
