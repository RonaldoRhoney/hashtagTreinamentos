faturamento =  input('Qual foi o faturamento: ')
custo = input('Qual foi custo: ')

if faturamento and custo:
    lucro = input(faturamento) - input(custo)
    print('O lucros foi de {}'.format(lucro))
else:
    print('Preencha o faturamento e o custo, corretamente !')
    