import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    # MULTIPLICAR OS NÚMEROS PELA CONTAGEM REGRESSIVA DE 10 E SOMAR
    soma_nove_digitos = 0
    valor = 10

    for string in nove_digitos:
        soma_nove_digitos += int(string) * valor
        valor -= 1

    # MULTIPLICAR O VALOR DA SOMA POR 10
    soma_multiplicada = soma_nove_digitos * 10


    # OBTER O RESTO DA DIVISÃO DA SOMA POR 11
    primeiro_digito = 0 if soma_multiplicada % 11 > 9 else soma_multiplicada % 11

    # CÁLCULO DO SEGUNDO DÍGITO DO CPF
    dez_digitos = nove_digitos + str(primeiro_digito)
    # print(f'Os dez primeiros dígitos do CPF são: {dez_digitos}')

    # Multiplicar os dígitos pela contagem regressiva de 11 e somar
    soma_dez_digitos = 0
    contador = 11

    for digito in dez_digitos:
        soma_dez_digitos += int(digito) * contador
        contador -= 1

    # print(f'A soma dos dez primeiros do CPF é: {soma_dez_digitos}')

    # Multiplicar a soma anterior por 10

    soma_multiplicada = soma_dez_digitos * 10
    # print(f'A multiplicação da soma por 10 é: {soma_multiplicada}')

    # Obter o resto da divisão da soma anterior por 11

    segundo_digito = 0 if soma_multiplicada % 11 > 9 else soma_multiplicada % 11


    cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    print(f'CPF {_ + 1} gerado: {cpf_gerado}')