qtdd_pessoas = int(input('Quantas pessoas tem no quarto: ?'))
quarto = []

for i in range(qtdd_pessoas):
    nome = input('Qual seu nome: ')
    cpf = input('Qual o seu CPF: ')
    hospedes = [nome, 'cpf: {}'.format(cpf)]

print(quarto)


# Análise de vendas:
 
meta = 1000
vendas = [
    ['Rhoney', 1598],
    ['Gilmar', 1201],
    ['Dom', 968],
    ['Dayan', 969],
    ['Ygor', 1001],
]
for item in vendas:
    if item[1] >= meta:
        print('vebdedor {} bateu a meta, ele fez: {}'.format(item[0], item[1]))
