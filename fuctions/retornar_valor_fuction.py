def cadastrar_produto():
    produto = input('Digite o produto: ')
    produto = produto.casefold()
    produto = produto.strip()
    return produto
prodoto = cadastrar_produto()
print('O produto {} foi cadsatrado com sucesso'.format(prodoto))