def eh_da_categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    return bebida.startswith(cod_categoria.upper())

# Lista de produtos com prefixos indicando categorias
produtos = ['BEB213', 'NAB147', 'BEB986', 'NAB235', 'OUT789']

# Verifica cada produto e direciona para o setor correto
for produto in produtos:
    if eh_da_categoria(produto, 'BEB'):
        print(f'Enviar {produto} para o setor de bebidas alcoólicas')
    elif eh_da_categoria(produto, 'NAB'):
        print(f'Enviar {produto} para o setor de bebidas não alcoólicas')
    else:
        print(f'Enviar {produto} para o setor geral')
