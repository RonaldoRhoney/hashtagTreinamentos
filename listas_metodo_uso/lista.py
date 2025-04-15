#Sempre criar listas homogêneas ou seja não misturar, ex: num, str, bool...

produtos = ['tv', 'mouse', 'teclado', 'geladeira']
vendas = [1500, 82, 199, 520, 97]

print(produtos, vendas)

print(produtos[1])
print(vendas[1])

print('Vendas do produto {} foram de {} unidades'.format(produtos[3], vendas[3]))

# modificando os valores dos produtos
vendas[2] = 800
print('Vendas do produto {} foram de {} unidades'.format(produtos[2], vendas[2]))



texto = 'ronaldorhoney@hotmail.com'
#texto[1] = '@' => essa aplicação dará erro
#texto.replace('h','q') => e essa não funciona
novo_texto = texto.replace('h', 'q')
print(novo_texto)

