vendas_tecnologia = {'Iphone': 1500, 'samsung': 12000, 'ps5': 14000, 'Ipad': 19600}

for chave in vendas_tecnologia:
    print(chave)
    print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))

# Cálculo do total de Iphones fora do primeiro loop
total_iphone = 0
for chave in vendas_tecnologia:
    if 'iphone' in chave.lower():  # Convertemos a chave para minúsculo para comparação
        total_iphone = total_iphone + vendas_tecnologia[chave]

print(f"\nTotal de iPhones vendidos: {total_iphone} unidades")