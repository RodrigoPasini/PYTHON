'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''
n1=float(input("Primeira nota: "))
n2=float(input("Segunda nota: "))
media=(n1+n2)/2
if media<5:
    print("Sua média é de {:.2f}.\n\033[41mREPROVADO!\033[m".format(media))
elif media>=5 and media<7:
    print("Sua média é de {:.2f}.\n\033[43mRECUPERAÇÃO!\033[m".format(media))
else:
    print("Sua média é de {:.2f}.\n\033[42mAPROVADO!\033[m".format(media))