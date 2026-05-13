# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))

print(f'Olá, {nome}! Seu nome possui {len(nome)} letras e daqui a 5 anos você terá a idade {idade + 5}.')
