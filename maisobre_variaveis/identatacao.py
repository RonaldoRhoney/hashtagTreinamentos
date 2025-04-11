meta = 0.05
taxa = 0
rendimento = 0.10

if rendimento > meta:
    if rendimento > 0.20:
        print('A taxa foi de {}'.format(taxa))
    else:
        taxa = 0.02
        print('A tax foi de {}'.format(taxa))
else:
    taxa = 0
    print('A taxa foi de {}'.format(taxa))

# trabalhando com elif:


mata = 20000
vendas = 28000

if vendas > meta:
    print('Não ganhou bonus')
elif vendas >  (meta * 2):
    bonus = 0.07 * vendas
    print('Ganhou {} de bonus'.format(bonus))
else:
    bonus = 0.03 * vendas
    print('Ganhou {} bonus'.format(bonus))

print('Fim do programa')