# Função para validar CPF com base nos dígitos verificadores
def validar_cpf(cpf):
    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    # Verifica se os dígitos calculados batem com os do CPF
    return cpf[-2:] == f"{digito1}{digito2}"

# Entrada do usuário
cpf = input('Digite o seu CPF: ')

# Limpeza dos caracteres
cpf = cpf.strip().replace('.', '').replace('-', '')

# Validação básica e completa
if len(cpf) == 11 and cpf.isnumeric():
    if validar_cpf(cpf):
        print('✅ CPF válido e cadastrado com sucesso:', cpf)
    else:
        print('❌ CPF inválido! Dígitos verificadores incorretos.')
else:
    print('⚠️ CPF inválido! Digite apenas os 11 números do seu CPF.')
