

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

i_maior_valor = vendas_1sem.index(maior_valor)
i_menor_valor = vendas_1sem.index(menor_valor)

print('O maior mês foi {} com {} vendas' .format(meses[i_maior_valor], maior_valor))
print('O pior mês foi {} com {} vendas'.format(meses[i_menor_valor], menor_valor))

fatu_total = sum(vendas_1sem)
print('O faturamento total foi de: R$ {}'.format(fatu_total))

percentagem = maior_valor / fatu_total

print('O melhor mês representa {:.2%} das vendas do ano'.format(percentagem))


# Agora vamos cria uma lista dos top produtos dessa lista:

top3 = []

print(vendas_1sem)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
print(top3)

#vendas_1sem.remove(maior_valor)
#print(vendas_1sem)

maior_valor = max(vendas_1sem)
print(maior_valor)
top3.append(maior_valor)

#vendas_1sem = max(maior_valor)
#print(top3)

maior_valor = max(vendas_1sem)
top3.append(maior_valor)
print(top3)
