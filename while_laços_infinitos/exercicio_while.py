vendas = []

while True:
    produto = input('Qual o produto?: ')
    if not produto:
        break
    qtdd = int(input('Qual a quantidade?: '))
    vendas.append([produto, qtdd])
print(vendas)