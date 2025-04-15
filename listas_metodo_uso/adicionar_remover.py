produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpod']
print(produtos)

# Adicionando um item na lista:

produtos.append('iphone 11')
print(produtos)

# Removendo um produto da lista

produtos.remove('iphone x')
print(produtos)

# Tratando erros:

produtos_remover  = 'iphone x'

if produtos_remover in produtos:
    produtos.remove('iphone x')
else:
    print('{} não existe este produto na lista de produtos'.format(produtos_remover))


    # O uso do TRY  e do EXEPT:

try:
    produtos_remover('iphone x')
    print(produtos)
except:
    print('iphonex não existe na lista de produtos')