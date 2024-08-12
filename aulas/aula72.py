'''
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar

RECOMENDADO - CRIAR O CÓDIGO EM INGLÊS
'''
# EXERCÍCIO 01 - MULTIPLICA VALORES
def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

valores = 10, 5, 32, 76, 20
variavel = multiplica(*valores)
verifica = 10 * 5 * 32 * 76 * 20

print(variavel)
if variavel == verifica:
    print('O resultado da função está correto!')
else:
    print('O resultado da função está incorreto!')

# EXERCÍCIO 02 - FALA SE UM NÚMERO É PAR OU ÍMPAR
def impar_ou_par(numero):
    if numero % 2 == 0:
        return f'O número {numero} é Par'
    return f'O número {numero} é Impar'

valor = 6
print(impar_ou_par(valor))
