import random

# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

estados_capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracajú',
    'Tocantins': 'Palmas'
}

dict_items = list(estados_capitais.items())
random.shuffle(dict_items)

acertos = 0
erros = 0

while dict_items:
    par_atual = dict_items.pop()
    estado_atual = par_atual[0].upper()
    cidade_atual = par_atual[1].upper()
    resposta = input(f'Qual a capital do Estado {estado_atual}? ')
    if resposta.upper() == cidade_atual:
        acertos += 1
    else:
        erros += 1
    continuar = input('Deseja continuar? [S/N]')
    if continuar.upper() in ['N', 'NÃO', 'NAO']:
        break

print(f'Você acertou {acertos}, ou seja, {(acertos * 100) / (acertos + erros):.2f}% de acertos!')






























