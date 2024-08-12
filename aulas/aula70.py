'''
Retorno de valores das funções (return)
Existem funções que não retornam valor algum: print
Existem funções que retornam valores: return
'''

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

# variavel = soma(1, 2) # print é uma função que retorna None
# variavel = int('1')

soma1 = soma(2, 2) # retorna 4
soma2 = soma(3, 3) # retorna 5

print(soma1 + soma2)
print(soma(11, 55))