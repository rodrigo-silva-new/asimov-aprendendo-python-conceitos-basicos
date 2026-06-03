### Métodos de Números
# .as_integer_ratio()
# Pega uma razão de números inteiros que vai gerar o valor informado
'''
x = 4.5
print(x.as_integer_ratio())
x = 38.125
print(x.as_integer_ratio())
'''





# .is_integer()
# Verifica se um número é inteiro (se é inteiro na representação do número, ou seja,
# se temos 4.0, ele vai considerar que é inteiro, já que, nesse caso, o 0 não tem valor
'''
x = 4.5
y = 4.0
print(x.is_integer())
print(y.is_integer())
'''







### Métodos de Strings
# Verificar os vários métodos de strings
'''
s = 'abc'
print(dir(s))
'''



# .upper() e .lower()
# Deixa todas as letras maiúsculas ou minúsculas
'''
palavra = 'Olá MunDo!'
print(palavra.upper())
print(palavra.lower())
'''



# .startswith() e .endswith
# Verificam se a string inicia ou finaliza com um determinado conjunto de caracteres
'''
arquivo = '2023_01_01_NotaFiscal.pdf'
print(arquivo.startswith('.docx'))
print(arquivo.startswith('2023'))
print(arquivo.endswith('.pdf'))
print(arquivo.endswith('.docx'))
'''



# .count()
# Conta quantas vezes um caractere ou sequência de caracteres aparece em uma string
'''
texto = 'Hoje em dia todo dia é um novo dia. Mais um dia chega. Dia!'
print(texto.count('a'))
print(texto.count('dia'))


# Encadeamento de métodos: quando usamos um método e logo na sequência, usamos outro
print(texto.lower().count('dia'))
'''








# .find()
# Retorna o índice da posição em que o caractere foi encontrado pela primeira vez
# Quando não encontra o caractere, ele retorna -1
#seq = 'aaaaaabaaaaaabaaaaaab'

#print(seq.find('b'))
#print(seq.find('c'))


# .index()
# Também retorna o índice do caractere, mas se não encontrar, retorna um erro (é mais restrito que o find)
#print(seq.index('b'))
#print(seq.index('c'))




# Slicing com find
# Fatiar da primeira ocorrência do caractere até o final da string
#print(seq[seq.find('b'):])







### Outros métodos

# .isdigit() e .isalpha()
# Retorna true se não tiver caracteres além de números na string
# Retorna true se não tiver caracteres além de letras na string
'''
s1 = '5245245234523'
s2 = 'adfadfasdfasdf'
s3 = 'Olá 2023 Python!'

print(s1.isdigit())
print(s2.isalpha())

print(s3.isdigit())
print(s3.isalpha())
'''







# .replaced()
# Troca um caractere por outro
'''
frase = 'Estou estudando Python!'

print(frase.replace('!', '?'))
print(frase.replace('u', '???'))
print(frase.replace('Python', 'JavaScript'))



frase2 = 'Estou estudando Python! \n\n\n Este curso é muito bom!'
print(frase2)
print(frase2.replace('\n', '').replace(' ', ''))
'''





## split e join
# .split()
# Divide a string em uma lista. Por padrão, a partir de espaços
'''
linha = 'Item1          Item2          Item3'
linha2 = 'Item1;Item2;Item3'

print(linha.split())
print(linha2.split(';'))
'''



# .join()
# Junta elementos de um iterável de strings, utilizando uma string separadora, gerando uma string final
nomes = ['Joana', 'Marcelo', 'Paulo']
print('-----'.join(nomes))





























