# 1 forma

meta = 10000
vendas = [
    ['João', 12000],
    ['Carlos', 798],
    ['Maria', 38312],
    ['Rhoney', 51200], 
    ['André', 1010]
]

acima_meta = []

for venda in vendas:
    if venda [1] >= meta:
        acima_meta.append(venda)
print(acima_meta)
print('{:.1%} dos vendedores bateram a meta'.format(len(acima_meta) / len(vendas)))

# 2 forma:

qtdd_vendedres = 0

for venda in vendas:
    if venda[1] >= meta:
        qtdd_vendedres = [1]
print('{:.1%} dos vendedores bateram a meta'.format(len(qtdd_vendedres) / len(vendas)))

# 3 forma:

melhor_vendedor = ''
maior_venda = 0

for venda in vendas:
    if venda[1] > maior_venda:
        maior_venda = venda[1]
        melhor_vendedor = venda[0]
print('O melhor vendedor foi {} com {} vendas'.format(melhor_vendedor, maior_venda))