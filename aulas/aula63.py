'''
Cálculo do segundo dígito do CPF
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF
MAIS O PRIMEIRO DÍGITO,
multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex.: 746.824.890-70

    11  10  09  08  07  06  05  04  03  02
    07  04  06  08  02  04  08  09  00  07 <- PRIMEIRO DÍGITO
    77  40  54  64  14  24  40  36  00  14

Somar todos os resultados:
70+40+54+64+14+24+40+36+0+14 = 363
Multplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é valor da conta

O segundo dígito do CPF é 0

'''
import re
import sys

entrada = input('CPF: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
)

print(f'O CPF sem ponto e traço é {cpf}')

# CÁLCULO DO PRIMEIRO DÍGITO DO CPF
nove_digitos = cpf[:9]
# print(f'Os nove primeiros dígitos do CPF são: {nove_digitos}')

# VERIFICAR SE O CPF NÃO TEM SOMENTE STRINGS REPETIDAS

entrada_sequencia = entrada == entrada[0]*len(entrada)

if entrada_sequencia:
    print('Você enviou caracteres repetidos no CPF')
    sys.exit()



# MULTIPLICAR OS NÚMEROS PELA CONTAGEM REGRESSIVA DE 10 E SOMAR

soma_nove_digitos = 0
valor = 10

for string in nove_digitos:
    soma_nove_digitos += int(string) * valor
    valor -= 1
# print(f'O valor da soma é: {soma_nove_digitos}')
# MULTIPLICAR O VALOR DA SOMA POR 10

soma_multiplicada = soma_nove_digitos * 10
# print(f'O valor da multiplicação é: {soma_multiplicada}')
# OBTER O RESTO DA DIVISÃO DA SOMA POR 11

primeiro_digito = 0 if soma_multiplicada % 11 > 9 else soma_multiplicada % 11

print(f'O primeiro dígito calculado do CPF é: {primeiro_digito}')

if primeiro_digito == int(cpf[9]):
    print(f'O primeiro dígito do CPF está correto, pois {primeiro_digito} = {int(cpf[9])}')
else:
    print(f'O primeiro dígito do CPF não está correto, pois {primeiro_digito} != {int(cpf[9])}')

# CÁLCULO DO SEGUNDO DÍGITO DO CPF
dez_digitos = cpf[:10]
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
print(f'O segundo dígito do CPF é: {segundo_digito}')

if segundo_digito == int(cpf[10]):
    print(f'O segundo dígito do CPF está correto pois {segundo_digito} = {int(cpf[10])}')
else:
    print(f'O segundo dígito do CPF está incorreto pois {segundo_digito} != {int(cpf[10])}')


# VERIFICAR A VALIDAÇÃO DO CPF

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
print(f'CPF gerado: {cpf_gerado}')

if cpf_gerado == cpf:
    print('O CPF é válido.')
else:
    print('O CPF é inválido.')