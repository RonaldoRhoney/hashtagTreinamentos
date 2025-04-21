vendas = ('Rhoney', '14/08/1992', '15/02/2015', 2500, 'Dev Python')
print(vendas)

nome, data_contratacao, data_nascimento, salario, cargo = vendas
print(cargo)

vendas = [1000, 2000, 300, 350, 150]
funcionarios = ['Rhoney', 'Dom', 'Gilmar', 'Ygor', 'Dayan']
for i, venda in enumerate(vendas):
    print('{} vendeu {} unidades'. format(funcionarios[i], venda))