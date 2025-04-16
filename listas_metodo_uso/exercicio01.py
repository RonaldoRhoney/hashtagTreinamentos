

meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]
vendas_1sem = [2500, 2690, 82000, 7500, 950, 3964]
vendas_2sem = [4100, 542, 8579, 3520, 800, 940]

vendas_1sem.extend(vendas_2sem)

maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)

print(vendas_1sem)
print(maior_valor)
print(menor_valor)