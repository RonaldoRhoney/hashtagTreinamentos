vendedores = ['João', 'Pedro', 'lucas', 'Ana']
vendas = [100, 150, 1500, 2000, 120]
meta = 130

for venda in vendas:
    if venda < meta:
        continue
    print(venda)