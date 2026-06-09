## Alguns métodos que funcionam e já foram vistos em "Métodos de Strings e Números":
# Tuplas
'''
tup = (0, 0, 0, 1, 0, 1, 0)

print(tup.index(1))
#print(tup.index(9))

print(tup.count(0))


# Listas
l1 = [0, 0, 1, 0, 1, 0]
l2 = l1.copy()

l1.clear()
print(l1)
print(l2)
'''




### Métodos de listas:
# .append()
# Adiciona um elemento ao final de uma lista
# Obs: se tentar adicionar outra lista a uma lista, a lista inteira será adicionada como um único elemento
'''
l1 = [0, 0, 1, 0, 1, 0]
l2 = l1.copy()

l1.clear()
print(l1)

for n in range(5):
    l1.append(n * 2)

print(l1)

l1.append('hello')
print(l1)


valores = [10, 30, -90, -1, 0, 1]

valores_positivos = []

for valor in valores:
    if valor > 0:
        valores_positivos.append(valor)

print(valores_positivos)
'''






# .extend()
# Estende uma lista com os elementos de outra lista
# Esse método trabalha na própria lista, sem criar uma nova
'''
numeros = [1, 2, 3]
numeros.extend([4, 5, 6])
print(numeros)



# É possível concatenar listas:
numeros = [1, 2, 3]
novos_numeros = numeros + [4, 5, 6]
print(numeros)
print(novos_numeros)





# .insert()
# Insere o elemento na posição indicada, empurrando os outros elementos para a direita
# Se colocar uma posição muito afastada, insere o elemento no início ou final
vogais = ['a', 'i', 'o', 'u']
vogais.insert(1, 'e')
print(vogais)

vogais.insert(1000, 'teste1')
vogais.insert(-1000, 'teste2')
print(vogais)
'''







# .pop()
# Remove um elemento da lista e o retorna
# Por padrão, remove o último elemento da lista
# É possível determinar a posição do item que quer remover e retornar
'''
valores = [150, 20, 30, 40, 50]

valor_removido = valores.pop()
print(valor_removido)
print(valores)

valor_removido2 = valores.pop(0)
print(valor_removido2)
print(valores)





clientes = ['xxx', 'yyy', 'zzz']

while clientes:
    cliente = clientes.pop()
    print(f'Processando cliente {cliente}')

'''










# .reverse()
# Inverte a lista
valores = [150, 30, 50, 75, 50, 30, 150]

valores.reverse()
print(valores)



# .sort()
# Ordena a lista do menor valor para o maior
valores.sort()
print(valores)






















