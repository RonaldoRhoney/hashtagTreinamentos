estoque = [1200, 600, 39, 180, 400, 49]
produtos = ['coca', 'guaraná', 'água', 'sprite', 'suco', 'vinho']

nivel_minimo = 50

for i, qtdd in enumerate(estoque):
    if qtdd < nivel_minimo:
        print('{} está abaixo do nível mínimo, temos apenas {} unidades'.format(produtos[i], qtdd))