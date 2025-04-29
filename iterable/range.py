funcionarios = ['Maria', 'João', 'Ana', 'Carlos']
vendas = [1750, 1980, 2100, 1930]

print('Funcionários Classe B')

for funcionario, venda in zip(funcionarios, vendas):
    print(f'{funcionario} fez {venda} vendas')

