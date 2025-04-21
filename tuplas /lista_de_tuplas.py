vendas = [
    ('20/08/2020', 'iphone x', 'Azul', '128gb', 300, 4000),
    ('20/08/2020', 'ipad', 'rosa', '64gb', 1500, 250),
    ('20/08/2020', 'motog50', 'prata', '168gb', 530, 4510),
    ('21/08/2020', 'samsung tv', 'preta', '500rps', 200, 2580),
    ('21/08/2020', 'cafeteira', 'Amarela', '15gb', 1590, 560),
    ('21/08/2020', 'notbook Dell', 'preto', '2tr', 600, 3500),
]
faturamento = 0

for item in vendas:
    data, produto, cor, capacidade, unidades, valor_uni = item

    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidades * valor_uni
print(f'O faturamento de iphone x no dia 20/08/2020 foi de: R$ {faturamento:,.2f}')
