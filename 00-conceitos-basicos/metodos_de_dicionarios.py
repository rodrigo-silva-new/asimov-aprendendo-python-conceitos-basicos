produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00,
}


# .clear()
# limpa o conteúdo do dicionário
#produtos.clear()

# .get()
# pega o valor e se não encontrar, pega um outro valor padrão
#print(produtos.get('banana'))
#print(produtos.get('arroz', 'não foi encontrado!'))


# .setdefault()
# faz o mesmo que o .get(), mas quando não acha a chave, adiciona o valor padrão no dicionário
#print(produtos.setdefault('banana', 100))
#print(produtos.setdefault('arroz', 100))
#print(produtos)


# .keys()
# Gera uma sequência das chaves do dicionário. Retorna uma visão das chaves.
#for produto in produtos.keys():
#    print(produto)


# .values()
# Gera uma sequência dos valores do dicionário. Retorna uma visão dos valores.
#for valor in produtos.values():
#    print(valor)



# .items()
# Gera uma sequência dos itens do dicionário. Retorna uma visão dos itens.
#for item in produtos.items():
#    print(item)

#algo comum é usar .items() e empacotamento, juntos:
#for k, v in produtos.items():
#    print(f'{k} -> {v}')









# .update()
# Atualiza um dicionário a partir de outro, ou seja,
# chaves novas são criadas e as iguais são atualizadas no dicionário original pelos valores do segundo
products = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão': 9.00,
}

new_products = {
    'massa': 5.70,
    'banana': 4.40,
}

#print(products)
#products.update(new_products)
#print(products)





# .copy()
# Cria uma cópia independente do dicionário,
# podendo alterar cada um sem interferência no outro
produtos_copia = produtos.copy()
produtos_copia['morango'] = 3.30
print(produtos)
print(produtos_copia)

























