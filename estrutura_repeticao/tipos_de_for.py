produtos = ['Iphone 11', 'Ipad', 'Airpod', 'Mac Book']
precos = [7000, 10000, 25000, 17000]

for preco in precos:
    print(preco * 1.1)


# Determinando o preço de cada produto com RANGE:

for i in range(len(precos)):
    produto = produtos[i]
    preco = precos[i]
    print(produto, preco)


# enumerate:

for i, preco in enumerate(precos):
    produto = produtos[i]
    print(produto, preco)