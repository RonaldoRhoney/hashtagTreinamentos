faturamento = 2500
faturamento1 = 2200
email = 'rhoneyhotmail.com'

print('PROGRAMA 01')

if faturamento == faturamento1:
    print('Os emais são iguais')
else:
    print('Os emails são diferentes')


print('PROGRAMA 02')

if email != 'rhoney@hotmail.com':
    print('Esse email não pertence ao Rhoney')
else: 
    print('Email errado !')


print('PROGRAMA 03')

email_usuario = input('Insira o seu email: ')
if not '@' in email_usuario:
    print('Email errado! ')
else:
    pass