


nome = input('Digite seu nome: ')
email = input('Digite seu email: ')

if nome and email:
    posicao_a = email.find('@')
    servidor = email[posicao_a:]
    if posicao_a != -1 and '.' in servidor:
        print('Cadastro realizado com sucesso !')
    else:
        print('Email inválido')
else:
    print('Digite seu nome e e-mail corretamente, por avor !!')