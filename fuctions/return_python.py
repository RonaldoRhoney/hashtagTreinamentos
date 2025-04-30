# Exemplo 1: return com soma
def minha_soma(num1, num2, num3):
    return num1 + num2 + num3

resultado_soma = minha_soma(10, 20, 30)
print('Resultado da soma:', resultado_soma)

# Exemplo 2: return com manipulação de texto
def padronizar_textos(texto):
    texto = texto.casefold()
    texto = texto.replace('  ', '')  # remove apenas dois espaços consecutivos
    texto = texto.strip()  # remove espaços nas pontas
    return texto

texto_formatado = padronizar_textos('Estou aprendendo Python')
print('Texto padronizado:{}'.format(texto_formatado))

# Exemplo 3: return com filtragem de lista
def filtrar_lista_texto(lista, pedaco_texto):
    lista_filtrada = []

    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada

nomes = ['Amanda', 'Camila', 'André', 'Raimundo', 'Anastácia', 'Fenanda']
nomes_com_and = filtrar_lista_texto(nomes, 'and')
print('Nomes contendo "and":{}'.format(nomes_com_and))

print('Fim do programa')

