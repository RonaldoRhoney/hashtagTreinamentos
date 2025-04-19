qtdd_pessoas = int(input('Quantas pessoas tem no quarto: ?'))
quarto = []

for i in range(qtdd_pessoas):
    nome = input('Qual seu nome: ')
    cpf = input('Qual o seu CPF: ')
    hospedes = [nome, 'cpf: {}'.format(cpf)]

print(quarto)