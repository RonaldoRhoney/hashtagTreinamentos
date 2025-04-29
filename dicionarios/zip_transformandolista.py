produtos = ['iphone', 'samsung galaxy', 'samsung tv', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook dell', 'notebook hp']
vendas = [1500, 12000, 1000, 4231, 1720, 1001, 2500, 17200, 2450]

# Criando o dicionário inicial com 0 vendas
dicionario = dict.fromkeys(produtos, 0)
print(dicionario)

# Lista de tuplas (agora convertendo em lista para não "secar")
lista_tuplas = list(zip(produtos, vendas))

# Imprimindo os pares
for item in lista_tuplas:
    print(item)

# Criando o dicionário de vendas
dicionario_vendas = dict(lista_tuplas)

print(dicionario_vendas)

# Calculando as vendas de Samsung TV:
indice = produtos.index('samsung tv')
print('Vendemos {} unidades de Samsung TV'.format(vendas[indice]))

print('Vendemos {} unidades de Samsung TV'.format(dicionario_vendas['samsung tv']))
