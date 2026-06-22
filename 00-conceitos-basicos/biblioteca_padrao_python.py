'''
import math

print(math.pi)

print(math.log(16, 2))
'''










'''
import datetime

agora  = datetime.datetime.now()

ano_2000 = datetime.datetime(2000, 1, 1)

print(agora - ano_2000)
'''









'''
import random

for _ in range(5):
    n = random.randint(1, 10)
    print(f'Número escolhido: {n}')




nomes = ['Juliano', 'Marcos', 'Paulo']

for _ in range(5):
    nome = random.choice(nomes)
    print(f'Nome escolhido: {nome}')
'''









'''
import os

print(os.getcwd()) # mostra de onde o Python tá sendo executado
print(os.listdir()) # Lista o diretório - Sem argumento, lista a pasta atual
'''













import time

inicio = time.time()

print('Primeira linha')

time.sleep(3) # Para o programa de executar por algum tempo (3s no exemplo)

print('Segunda linha')

final = time.time()

tempo_execucao = final - inicio
print(tempo_execucao)































