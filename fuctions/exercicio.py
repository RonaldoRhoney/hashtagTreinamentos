preco = 1500
custo = 400
lucro = 800

def carga_tributaria(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco
print('A carga tributária foi de: {:.1%}'.format(carga_tributaria(preco, custo, lucro)))