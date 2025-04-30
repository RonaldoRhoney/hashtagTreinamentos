produtos = ['ps5', 'aipod', 'apple tv', 'aplle watch', 'ipad', 'iphone x', 'mac book', 'mac ox']
produtos.sort()
print(produtos)

produtos.sort(reverse=True)
print(produtos)

# Função para padronizar códigos
def padronizar_codigos(lista_codigos, padrao='m'):
    for i, item in enumerate(lista_codigos):
        item = item.replace(" ", "")  # remove espaços internos
        item = item.strip()  # remove espaços nas extremidades

        if padrao == 'm':  # tudo minúsculo
            item = item.casefold()
        elif padrao == 'M':  # tudo maiúsculo
            item = item.upper()

        lista_codigos[i] = item
    return lista_codigos

# Testando a função
lista_codigos = ['AB12', 'acj34', 'abc37']
print(padronizar_codigos(lista_codigos, 'M'))  
  

