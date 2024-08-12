'''
Valores padrão para parâmetros
Ao definir uma função, os valores podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.

Refatorar: editar o seu código.
'''

def soma(x, y, z = None):
    if z is not None:
        print(f'{x=} {y=} {z=}. Soma =', x + y + z)
    else:
        print(f'{x=} {y=}. Soma =', x + y)

soma(1, 2)
soma(3, 5)
soma(150, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)


'''
Explicação:
- A função 'soma' recebe três argumentos: x, y e z.
- Se o valor de z não for fornecido, ele assume o valor None.
'''