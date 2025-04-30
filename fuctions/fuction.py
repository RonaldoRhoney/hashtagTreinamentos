def cadastra_produtos():
    produto = input('Digite o produto: ')
    produto = produto.casefold()
    print('O produto {} foi cadastrado com sucesso'.format(produto))

for i in range(3):
    cadastra_produtos()
    