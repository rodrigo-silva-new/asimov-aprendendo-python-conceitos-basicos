# Forma tradicional:
'''
valores = list(range(10))

maiores_que_cinco = []
for valor in valores:
    if valor > 5:
        maiores_que_cinco.append(valor)

print(valores)
print(maiores_que_cinco)
'''





# Compreensão de lista (list comprehension)
valores = list(range(10))

maiores_que_cinco = [valor for valor in valores if valor > 5]

print(valores)
print(maiores_que_cinco)
















