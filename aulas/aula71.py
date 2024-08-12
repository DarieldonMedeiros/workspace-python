'''
args - Argumentos não nomeados
* - * args (empacotamento e desempacotamento)
args - faz o empacotamento para uma tupla
* - desempacota a tupla
'''
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma (x, y):
#     return x + y

def soma(*args): # args faz o empacotamento para uma tupla
    total = 0
    for numero in args:
        total += numero
    return total

# soma1 = soma(1, 2, 3, 4, 5, 6)
# print(soma1)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

# print(sum((1, 2, 3, 4, 5, 6, 7, 78, 10)))
print(numeros)