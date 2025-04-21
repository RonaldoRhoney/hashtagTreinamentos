vendas = [100, 201, 810, 195, 72, 49, 88, 1000, 916]
vendedores = ['João', 'Carlos', 'Rhoney', 'Dom', 'Gilmar', 'Ana' 'Aline', 'Bia', 'Julia']
meta = 99
i = 0

while vendas[i] > meta:
    print('{} bateu a meta, vendeu {} unidades'.format(vendedores[i], vendas[i]))

    i += 1 # "interrompe o loop infinito"