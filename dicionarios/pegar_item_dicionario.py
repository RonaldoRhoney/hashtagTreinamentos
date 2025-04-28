mais_vendido = {'tecnologia': 'Iphone x', 'Refrigeracao': 'ar condicionado', 'livro': 'O poder de Python', 'eletrodomestico': 'geladeira'}
vendas_tecnologia = {'Iphone x': 1500, 'samsung': 12000, 'ps5': 14000}

vendas_refrigeracao = {'ar condicionado': 3200}

print('O produto mais vendido foi: {}'.format(mais_vendido['Refrigeracao']))

print('O livro mais vendido foi: {}'.format(mais_vendido['livro']))

print(vendas_tecnologia.get('Iphone x'))


print('Vendemos {} ar condicionado'.format(vendas_refrigeracao.get('ar condicionado')))

# verifica se um item está no dicionário 
if 'copo' in vendas_tecnologia:
    print(vendas_tecnologia['copo'])
else:
    print('Copo não está na categoria, tecnologia')
# verifica se um item está no dicionário
if vendas_tecnologia.get('copo') == None:
    print('Copo não está na categoria, tecnologia')


if vendas_tecnologia.get('copo') == None:
    print('Copo não está na categoria tecnologia')
else:
    print(vendas_tecnologia.get('copo'))
    
