#for i in range(5):
 #   print(i)

produtos = ['coca', 'pepsi', 'guaraná', 'sprite', 'fanta']
producao = [1500, 1200, 1300, 501, 350]
tamanho = len(produtos)

for i in range(tamanho):
    print('{} unidades produzidas de {}'.format(producao[i], produtos[i]))