#capitalize:
texto = 'rhoney'
print(texto.capitalize())

#casefold:
texto = 'Rhoney'
print(texto.casefold())

#count:
texto = 'ronaldorhoney@hotmail.com'
print(texto.count('o'))

# endwith

texto = 'ronadorhoney@hotmail.com'
print(texto.endswith('hotmail.com'))

#find
texto = 'ronaldorhoney@hotmail.com'
print(texto.find('@'))

#format
faturamento = 1100
print('O faturamento foi de {} Reais'.format(faturamento))

#isalnum
texto = 'rhon23598'
print(texto.isalnum())

#isalpha
texto = 'Rhoney01'
print(texto.isalpha())

#isnumeric
texto = '1298p53'
print(texto.isnumeric())

#replace
texto = '100.115'
print(texto.replace('.',','))

#split
texto = 'rhoney@hotmail.com'
print(texto.split('@'))

#splitlines
texto = '''Olá, bom dia!
        venho por meio deste tarzer o valor 
        do faturamento do dia. 
        Faturamento R$ = 20.000'''
print(texto.splitlines())

#startswith
texto = 'FADR85469'
print(texto.startswith('FAD'))

#strip
texto = '  BECA5555586  '
print(texto.strip())

#title
texto = 'ronaldo rhoney'
print(texto.title())

#upper
texto = 'adr2356'
print(texto.upper())