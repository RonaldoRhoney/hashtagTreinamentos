meta_funcionario = 10000
meta_loja = 25000
venda_funcionario = 15000
venda_loja = 20000

if venda_funcionario > meta_funcionario and venda_funcionario > venda_loja:
    bonus = 0.03 * venda_funcionario
    print('O bonus do funcionário foi de {}'.format(bonus))

else:
    print('Funcionário não ganhou bonus')


nota_funcionario = 9
meta_nota = 8

if nota_funcionario >= meta_nota or (venda_funcionario > meta_funcionario and venda_loja > meta_loja):
    bonus = 0.03 * venda_funcionario
    print('Bonus do funcionário foi de {}'.format(bonus))
else: print('O funcionário não ganhou bonus')