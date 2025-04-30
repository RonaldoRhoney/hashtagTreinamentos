def ehalcoolico(bebidas):
    bebidas = bebidas.upper()
    if 'BEB' in bebidas:
        return True
    else:
        return False
produtos = ['beb123', 'baxo6321', 'ocs85470', 'beb0124', 'car2154', 'beb2314']

for produto in produtos:
    if ehalcoolico(produto):
        print('Enviar {} para setor de bebidas alcólicas'.format(produto))