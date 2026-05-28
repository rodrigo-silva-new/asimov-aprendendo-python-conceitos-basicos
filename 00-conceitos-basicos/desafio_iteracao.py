# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !
numeros1 = [10, 3, 2, 22, 5, 8]
soma = 0

for n in numeros1:
    soma += n

print(f'A soma dos valores é {soma} e a média é {soma / len(numeros1):.1f}')


# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !
maior_numero = 0

for m in numeros1:
    if m > maior_numero:
        maior_numero = m

print(f'O maior número da sequência é {maior_numero}')


# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

lista_palavras = ['casa', 'chaveiro', 'pá', 'senha', 'português', 'pão', 'pano']

for c in lista_palavras:
    if len(c) >= 5:
        print(c)






