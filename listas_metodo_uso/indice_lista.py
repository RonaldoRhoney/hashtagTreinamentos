
#  Faça um programa de como descobrir o ÍNDICE de um ítem de uma lista:

produtos = ['tv','celular', 'tablet', 'mouse', 'geladeira', 'fogão', 'forno microondas']
estoque = [100, 109, 200, 321,49, 415, 87]

i = produtos.index('mouse')
print(i)
print(produtos[i])

qtdd_estoque = estoque[i]
print(qtdd_estoque)


# Programa para consultar o estoque:

produto = input('Insira o nome do produto em letras minúsculas: ')

if produto in produtos:
    i = produtos.index(produto)
    qtdd_estoque = estoque[i]
    print('Temos {} unidades de {} no estoque'.format(qtdd_estoque, produto))
else:
    print('{} não existe este produto no estoque'.format(produto))
