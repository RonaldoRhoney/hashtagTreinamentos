vendas = []  # Lista que vai armazenar os produtos

produto = input('Registre um produto. Para cancelar o registro, aperte Enter com a caixa vazia: ')

while produto != '':
    vendas.append(produto)
    produto = input('Registre um novo produto: ')

print('Registro finalizado. Os produtos registrados foram:', vendas)
