'''
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva de 10
Ex.: 746.824.890-70
    10 09 08 07 06 05 04 03 02
    07 04 06 08 02 04 08 09 00
    70 36 48 56 12 20 32 27 00

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

'''

cpf = '021.868.323-56'
cpf_formatado = cpf
# separa o CPF em dígitos
remover_caracteres = ['.', '-']

for string in remover_caracteres:
    cpf_formatado = cpf_formatado.replace(string, '')

print(f'O CPF sem ponto e traço é {cpf_formatado}')

nove_digitos = cpf_formatado[:9]
print(f'Os nove primeiros dígitos do CPF são: {nove_digitos}')

# MULTIPLICAR OS NÚMEROS PELA CONTAGEM REGRESSIVA DE 10 E SOMAR

soma_nove_digitos = 0
valor = 10

for string in nove_digitos:
    soma_nove_digitos += int(string) * valor
    valor -= 1
print(f'O valor da soma é: {soma_nove_digitos}')
# MULTIPLICAR O VALOR DA SOMA POR 10

soma_multiplicada = soma_nove_digitos * 10
print(f'O valor da multiplicação é: {soma_multiplicada}')
# OBTER O RESTO DA DIVISÃO DA SOMA POR 11

primeiro_digito = 0 if soma_multiplicada % 11 > 9 else soma_multiplicada % 11

print(f'O primeiro dígito calculado do CPF é: {primeiro_digito}')

if primeiro_digito == int(cpf_formatado[9]):
    print(f'O primeiro dígito do CPF está correto, pois {primeiro_digito} = {int(cpf_formatado[9])}')
else:
    print(f'O primeiro dígito do CPF não está correto, pois {primeiro_digito} != {int(cpf_formatado[9])}')
