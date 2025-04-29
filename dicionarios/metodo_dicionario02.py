vendas_tecnologia = {
    'notbook': 2450,
    'iphone': 1720,
    'samsung': 12000,
    'samsung tv': 1000,
    'ps5': 14300,
    'tablet': 1720,
    'notbook Dell': 1700,
    'ipod': 1201,
    'tv philco': 2500,
    'notebook hp': 10010
}

# Obtendo chaves e valores
chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()

print(chaves)
print(valores)

# Adicionando novo item ao dicionário
vendas_tecnologia['rhoney_phone'] = 10
print(chaves)
print(valores)

print('-' * 40)

# Imprimindo os itens (sem ordenação)
for chave in vendas_tecnologia:
    print(f'{chave}: {vendas_tecnologia[chave]} unidades')

print('-' * 40)

# Agora imprimindo os itens ordenados pelas chaves
lista_chaves = list(vendas_tecnologia.keys())
lista_chaves.sort()

for chave in lista_chaves:
    print(f'{chave}: {vendas_tecnologia[chave]} unidades')
