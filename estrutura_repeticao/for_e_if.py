vendas = [1001, 495, 1600, 2011, 800, 490, 1010, 8000]
meta = 1000

qtdd_bateu_meta = 0

for venda in vendas:
    if venda >= meta:
        qtdd_bateu_meta += 1

qtdd_funcionarios = len(vendas)

print('O percentual de vendas que batemos a meta foi de {:.1%}'.format(qtdd_bateu_meta / qtdd_funcionarios))
