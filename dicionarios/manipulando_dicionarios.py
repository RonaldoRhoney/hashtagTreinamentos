lucro_1trim = {'janeiro': 10000, 'fevereiro': 120000, 'maio':90000}
lucro_2trim = {'abril': 88000, 'marco': 89000, 'junho': 120000}

# adicionando 1 item 

lucro_1trim['abril'] = 88000

print(lucro_1trim)

# Adicionando vários itens:

lucro_1trim.update(lucro_2trim)
print(lucro_1trim)

# Adicionando item que já existe no dicionário:

lucro_1trim['fevereiro'] = 10000
print(lucro_1trim)

#modificando um item do dicionário:

lucro_fev = 85000
lucro_1trim['fevereiro'] = lucro_fev
print(lucro_1trim)


# Removendo um item do dicionário:

del lucro_1trim['janeiro']
print(lucro_1trim)

lucro_mar = lucro_1trim.pop('marco')
print(lucro_1trim)
print(lucro_mar)