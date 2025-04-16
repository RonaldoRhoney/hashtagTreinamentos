lista = ['maçã', 'goiaba']
vendas = [1500, 250]

lista += ['laranja']
print(lista)

soma_vendas = 300
soma_vendas += 300
print(soma_vendas)

email = 'Esse mês vendemos um total de {} produtos, sendo: \n {} unidade de {}\n {} unidades de {}'.format(soma_vendas, vendas[0], lista[0], vendas[1], lista[1])
print(email)