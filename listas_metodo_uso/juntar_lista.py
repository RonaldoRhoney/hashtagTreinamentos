produtos = ['água', 'feijão', 'macarrão', 'soja']
print(produtos)
novos_produtos = ['cebola', 'carne', 'peixe']

produtos.extend(novos_produtos)
print(produtos)

todos_produtos = produtos + novos_produtos
print(todos_produtos)

# somando ...

vendas = [100, 1500, 15000, 20000, 985, 458, 101, 1234]
vendas_iphonex = [15000]
vendas_iphone11 = [20000]
tota_vendas = vendas[2] + vendas[3]
print(tota_vendas)


total_vendas_lista = vendas_iphonex + vendas_iphone11

print(total_vendas_lista)

#Ordenando lista:

produtos.sort()
print(produtos)

vendas.sort()
print(vendas)


