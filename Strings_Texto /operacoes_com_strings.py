faturamento = 1000
custo = 600
lucro = faturamento - custo

print('O faturamento da loja foi de:', faturamento, 
      'O custo da loja foi de:', custo, 
      'O lucro da loja foi de:', lucro)


# FORMAT:
print('O faturamento foi {} o custo foi de {} e o lucro foi de {}'.format(faturamento, custo, lucro))

#%d e %s:

print('O faturamento foi de %d, o custo foi de %d e o lucros foi de %d' %(faturamento, custo, lucro))

#usando o IN:

print ('@' in 'ronaldohotmail.com')
print('@' in 'ronaldorhoney@hotmail.com')