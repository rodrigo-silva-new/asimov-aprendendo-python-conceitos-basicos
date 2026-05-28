# Dado duas listas, printe todos os valores que aparecem
# duplicados nas duas listas.

lista1 = [1, 3, 8, 11, 21, 32]
lista2 = [1, 4, 9, 21, 7]

for valor1 in lista1:
    for valor2 in lista2:
        if valor1 == valor2:
            print(valor1)


# Dado duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.

sequencia1 = [1, 3, 5, 7]
sequencia2 = [2, 4, 6, 8]

elemento_comum = False

for numero1 in sequencia1:
    for numero2 in sequencia2:
        if numero1 == numero2:
            elemento_comum = True
            print('Existe pelo menos um elemento em comum')
            break
        else:
            continue
if elemento_comum == False:
    print('Não existe elemento em comum.')








