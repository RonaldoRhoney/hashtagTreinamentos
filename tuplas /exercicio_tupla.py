meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

for vendedor, qtde in vendas:
    if qtde >= meta:
        print('{} bateu a meta, vendeu {} unidades'.format(vendedor, qtde))

## 2. Comparação com Ano Anterior

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

#seu código aqui
for produto, vendas2019, vendas2020 in vendas_produtos:
    if vendas2020 > vendas2019:
        crescimento = vendas2020 / vendas2019 - 1
        print('{} teve {} vendas em 2019, {} vendas em 2020. Crescimento de {:.1%}'.format(produto, vendas2019, vendas2020, crescimento))