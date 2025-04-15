custo = 500
faturamento = 10190
lucro = faturamento - custo
print('Faturamneto foi de R$ {:+} e o lucro foi de R$ {:+}'.format(faturamento, lucro))

print('Faturamento foi de {:.2f} e o lucro {:.3f}'.format(faturamento, lucro))

margem = lucro / faturamento
print('Margem de lucro foi de {:.2%}'.format(margem))


print('Faturamento foi de R$ {:,.2f} e o lucro foi de R$ {:,.2f}'.format(faturamento, lucro))

imposto = 0.125322
preco = 100
valor_imposto = round(preco * imposto, 1)
print('Imposto sobre o preço é de R$ {}'.format(valor_imposto))
