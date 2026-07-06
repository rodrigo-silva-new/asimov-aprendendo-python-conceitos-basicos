# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 2 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'

cifra = 'abcA*zy'
chave = 2

texto_cifrado = ''

def cifrador_de_texto(alfabeto, caractere, chave):
    index_inicial = alfabeto.index(caractere)
    index_final = index_inicial + chave
    if (index_final) <= (len(alfabeto) - 1):
        return index_final
    else:
        return index_final - (len(alfabeto))


for caractere in cifra:
    if caractere in maiusculas:
        index_atualizado = cifrador_de_texto(maiusculas, caractere, chave)
        texto_cifrado += maiusculas[index_atualizado]
    elif caractere in minusculas:
        index_atualizado = cifrador_de_texto(minusculas, caractere, chave)
        texto_cifrado += minusculas[index_atualizado]
    else:
        texto_cifrado += caractere

print(f'O texto cifrado é: {texto_cifrado}')












































