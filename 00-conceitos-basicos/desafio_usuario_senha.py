# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variáveis dentro do próprio código.


# MINHA VERSÃO:
#usuario_correto = 'Pedro'
#senha_correta = 'senha secreta'

#usuario_digitado = input('Digite o nome do usuário: ') == usuario_correto
#senha_digitada = input('Digite a senha: ') == senha_correta

#if usuario_correto and senha_digitada:
#    print('Você conseguiu acessar o sistema!')
#elif not usuario_digitado:
#    print('Usuário incorreto!')
#elif not senha_digitada:
#    print('Senha incorreta!')










# VERSÃO DO PROFESSOR:
usuario_correto = 'Pedro'
senha_correta = 'senha secreta'

usuario = input('Nome do usuário: ')
senha = input('Senha: ')

if usuario == usuario_correto:
    if senha == senha_correta:
        print(f'Acesso liberado, seja bem-vindo(a) {usuario}')
    else:
        print(f'Senha incorreta para o usuário {usuario}')
else:
    print(f'Usuário {usuario} não cadastrado no sistema')










