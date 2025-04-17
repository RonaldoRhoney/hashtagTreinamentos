

vendedores = ['Dayan', 'Gilmar', 'Dom', 'Rhoney']
produtos = ['iphone', 'apple tv', 'aipd', 'mac book']
vendas = [
    [1500, 350],
    [196, 391],
    [412, 187],
    [815, 101,]
]

# Quantos Gilmar vendeu de Iphone ?
# Quanto Dayan vendeu de Apple tv ?
# Qual o total de vendas de Iphone ?

vendas_iphone_gilmar = vendas[1] [0]
print(vendas_iphone_gilmar)

vendas_appletv_dayan = vendas[0] [1]
print(vendas_appletv_dayan)

vendas_iphone = vendas[0][0] + vendas[1][0] + vendas[2][0] + vendas[3][0]
print(vendas_iphone)

# digamos que o vendedor Dayan vendeu apenas 39 Apple Tv...

vendas[0][1] = 39
print(vendas)

# Agora vamos adicionar um outro produto para ser vendido: Apple Wacth

vendas_applewatch = [60, 15, 80, 99]

vendas[0].append(vendas_applewatch[0])
vendas[1].append(vendas_applewatch[1])
vendas[2].append(vendas_applewatch[2])
vendas[3].append(vendas_applewatch[3])

print(vendas)
