vendas_tecnologia = {'notbook': 2450, 'iphone':1720, 'samsung': 12000, 'samsung tv':1000, 'ps5': 14300, 'tablet': 1720, 'notbook Dell': 1700, 'ipod': 1201, 'tv philco': 2500, 'notebook hp': 10010}

itens_dicionario = vendas_tecnologia.items()
print(itens_dicionario)

for produto, qtdd in vendas_tecnologia.items():
    print('{}: {} unidades '.format(produto, qtdd))


#Quantos produtos venderam mais de 5000 unidades ?

for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print('{}: venderam mais de 5000, com um total de:  {} unidades'.format(chave, vendas_tecnologia[chave]))


# Outras forma de saber, é:

for produto, qtdd in vendas_tecnologia.items():
    if qtdd > 5000:
        print('{}: venderam mais de 5000, com um total de:  {} unidades'.format(produto, qtdd))