vendas_funcinario01 = 1000
vendas_funcinario02 = 750
vendas_funcinario03 = 1240

if vendas_funcinario01 >= 1000:
    print('O funcionário 1 ganho  {} de bonus'.format(vendas_funcinario01 *0.1))

if vendas_funcinario02 >= 1000:
    bonus = vendas_funcinario02 * 0.1
else:
    bonus = 0
    print('O funcionário 2 ganhou {} de bonus'.format(bonus))

if vendas_funcinario03 >= 1000:
    bonus = vendas_funcinario03 * 0.1
else:
    bonus = 0
    print('O funcionário 3 ganhou {} de bonus'. format(bonus))

if vendas_funcinario02 >= 2000:
    bonus = 0.15 *vendas_funcinario02
elif vendas_funcinario02 >= 1000:
    bonus= 0.1 * vendas_funcinario02
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bonus'.format(bonus))