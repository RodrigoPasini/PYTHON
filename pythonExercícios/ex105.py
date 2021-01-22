'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''
def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas o alun (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    r={}
    r['Total']=len(n)
    r['Maior']= max(n)
    r['Menor']= min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média']>=7:
            r['Situação'] = 'BOA'
        elif r['Média']>=5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'

    return r




resp=notas(9, 10, 5.5, 2.5, 6.5, sit=True)
print(resp)
help(notas)