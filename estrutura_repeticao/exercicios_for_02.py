# Exercícios

## 1. Criando um Registro de Hóspedes

#Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

#1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
#2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
#3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:
quarto = [
    ['João', 'cpf:00000000000'],
    ['Julia', 'cpf:11111111111'],
    ['Marcus', 'cpf:22222222222'],
    ['Maria', 'cpf:33333333333'],
]
#- Para simplificar, não vamos nos preocupar com possibilidades de "tentar colocar mais de 1 hóspede, digitar o cpf errado, etc. Nosso objetivo é treinar a criação de uma rotina de cadastro

#seu código aqui
qtde_pessoas = int(input('Quantas pessoas terão no quarto?'))
quarto = []

for i in range(qtde_pessoas):
    nome = input('Qual o nome?')
    cpf = input('Qual o cpf?')
    hospede = [nome, 'cpf:{}'.format(cpf)]
    quarto.append(hospede)
    
print(quarto)


meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
#seu código aqui
for item in vendas:
    if item[1] >= meta:
        print('Vendedor {} bateu a meta. Fez {} vendas'.format(item[0], item[1]))


produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
#seu código aqui

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        crescimento = vendas2020[i] / vendas2019[i] - 1
        print('{} vendeu R${:,} em 2019, R${:,} em 2020 e teve {:.1%} de crescimento'.format(produto, vendas2019[i], vendas2020[i], crescimento))