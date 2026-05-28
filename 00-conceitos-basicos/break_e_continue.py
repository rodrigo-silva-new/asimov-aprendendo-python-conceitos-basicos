n = 0

while n < 10:
    print(f'O valor de n é: {n}')
    n += 1
    if n == 5:
        break

print('O loop acabou')




for n in range(-5, 6):
    if n == 0:
        continue
    resultado = 1 / n
    print(resultado)

print('O loop acabou')





while True:
    entrada = input('Digite qualquer coisa ("q" para sair): ')
    print(f'O valor digitado foi {entrada}')
    if entrada == 'q':
        break

print('Programa finalizado')













