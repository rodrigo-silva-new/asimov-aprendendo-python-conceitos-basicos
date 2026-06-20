# None é um valor próprio, específico. Represent a ausência de valor.
# Muito usado como valor sentinela, pra informar que uma operação falhou (exemplo, o arroz no dic produtos).
'''
produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00,
}

print(produtos.get('banana'))
print(produtos.get('pão'))
print(produtos.get('arroz'))
'''




# Qualquer função que não tiver um "return" explícito, retorna None
'''
def dizer_ola():
    print('Olá!')

retorno = dizer_ola()
print(retorno)
'''




# Muitas funções básicas de Python retornam None
'''
retorno = print('Olá')
print(retorno)
'''




# Alguns métodos também retornam None (principalmente os mutáveis):

lista = [1, 2, 3]

retorno = lista.append(4)

print(lista)
print(retorno)
























