produtos = ['apple tv', 'maça', 'cebola', 'celular', 'mac book', 'android', 'agua']
tamanho = len(produtos)
print('Temos {} produtos'.format(tamanho))

# max e mim:

vendas = [120, 650, 250, 321, 150, 569, 900]
mais_vendido = max(vendas)
menos_vendido = min(vendas)

print('O produto mais vendido {} unidades e o menos vebdido {} unidades vendidos'.format(mais_vendido, menos_vendido))

i = vendas.index(mais_vendido)
produto_mais_vendido = produtos[i]
print('{} foi o produto mais vendido'.format(produto_mais_vendido))

i = vendas.index(menos_vendido)
produto_menos_vendido = produtos[i]
print('{} foi o roduto menos vendido'.format(produto_menos_vendido))


