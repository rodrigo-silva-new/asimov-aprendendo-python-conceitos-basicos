'''
def somar_dois(n):
    return n + 2


x = 10

resultado = somar_dois(x)

print(resultado)
'''







'''
# Obs: argumentos com valor padrão só podem vir depois de todos os argumentos sem padrão
def adicionar_final(texto, final="!!!"):
    return texto + final



print(adicionar_final('Olá', '!'))
print(adicionar_final('Olá'))
'''









'''
def dividir(a, b):
    if b == 0:
        return 'Impossível dividir!'
    return a / b


print(dividir(10, 5))
print(dividir(b=10, a=0)) # É possível chamar o nome do parâmetro em qualquer ordem, se especificar os valores
'''







# Exemplo de função com vários parâmetros:
def funcao_complexa(param_1=0, param_2=0, param_3=0, param_4=0):
    return param_1 + param_2 + param_3 + param_4


print(funcao_complexa(param_3=10))















