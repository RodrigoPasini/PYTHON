'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Coritiba.'''
times=("São Paulo", "Atlético-MG", "Flamengo", "Internacional", "Grêmio"
             "Palmeiras", "Fluminense", "Santos", "Corinthians", "Ceará",
            "Athletico-PR", "Atlético-GO", "Bragantino", "Fortaleza",
            "Sport", "Bahia", "Vasco", "Goiás", "Botafogo", "Coritiba")
print("-="*20)
print(f"Lista de times: {times}")
print("-="*20)
print(f"Os cinco primeiros times do Brasileirão são: {times[0:5]}")
print("-="*20)
print(f"Os quatro últimos colocados são: {times[-4:]}")
print("-="*20)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-="*20)
print(f"O Coritiba está na {times.index('Coritiba')+2} posição")
