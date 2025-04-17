produtos = ['computador', 'livro', 'tablet', 'celular', 'notbook', 'alexa', 'kindle']
produto_ecomerce = [
    [1000, 2500],
    [5000, 40],
    [180, 340],
    [2000, 390],
    [200, 190],
    [89, 49],
    [400, 1001],
    [100, 8002],
]
qtdd = 50000
preco = 40
total = qtdd * preco
print('{:,}'.format(total))

if 'livro' in produtos:
    i_livro = produtos.index('livro')

    total_antigo = produto_ecomerce[i_livro][0] * produto_ecomerce[i_livro][1]
    produto_ecomerce[i_livro][1] = produto_ecomerce[i_livro][1] * 1.1

    novo_total = produto_ecomerce[i_livro][0] * produto_ecomerce[i_livro][1]

    print('Vamos pagar de imposto a mais o valor de R$ {:,}'.format(novo_total - total_antigo))