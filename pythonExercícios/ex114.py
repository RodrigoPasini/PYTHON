#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
from urllib import request
try:
    site=urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site PUDIM não está disponível no momento =(')
else:
    print('Consegui acessar o site PUDIM com sucesso =D')
