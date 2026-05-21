# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

numero_secreto = 8

primeiro_chute = int(input('Digite aqui o seu primeiro número: '))
if primeiro_chute == numero_secreto:
    print(f'Você acertou o número! O número secreto é {numero_secreto}')
else:
    if primeiro_chute > numero_secreto:
        print(f'Você errou! O número secreto é menor do que {primeiro_chute}')
    elif primeiro_chute < numero_secreto:
        print(f'Você errou! O número secreto é maior do que {primeiro_chute}')
    segundo_chute = int(input('Digite aqui o seu primeiro número: '))
    if segundo_chute == numero_secreto:
        print(f'Você acertou o número! O número secreto é {numero_secreto}')
    else:
        if segundo_chute > numero_secreto:
            print(f'Você errou! O número secreto é menor do que {segundo_chute}')
        elif segundo_chute < numero_secreto:
            print(f'Você errou! O número secreto é maior do que {segundo_chute}')
        terceiro_chute = int(input('Digite aqui o seu primeiro número: '))
        if terceiro_chute == numero_secreto:
            print(f'Você acertou o número! O número secreto é {numero_secreto}')
        else:
            if terceiro_chute > numero_secreto:
                print(f'Você errou! O número secreto é menor do que {terceiro_chute}')
            elif terceiro_chute < numero_secreto:
                print(f'Você errou! O número secreto é maior do que {terceiro_chute}')






















