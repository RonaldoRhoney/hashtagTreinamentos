produto = input('Qual é o produto? ')
categotia = input('Qual é a categoria? ')
qtdade = input('Qual é a quantidade? ')

if produto and categotia and qtdade:
    qtdade = int(qtdade)
    if categotia == 'bebidas':
        if qtdade < 75:
            print('Solicite {} à equipe de vendas, temos apenas {}unidades em estoque'.format(produto, qtdade))
    if categotia == 'limpeza':
        if qtdade < 30:
             print('Solicite {} à equipe de vendas, temos apenas {}unidades em estoque'.format(produto, qtdade))     
    else:
        if qtdade < 50:
             print('Solicite {} à equipe de vendas, temos apenas {}unidades em estoque'.format(produto, qtdade))
else:('Preencha todas as informações')
                  
print('Fim do programa')
