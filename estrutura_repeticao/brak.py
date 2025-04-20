vendas = [100, 150, 1500, 2000, 120]
meta = 110

for venda in vendas:
    if venda < meta:
        print('A loja não ganhou bonus')
        break
    print(venda)


