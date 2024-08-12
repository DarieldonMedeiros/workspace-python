'''Calculadora com while'''
# somente as 4 operações básicas


while True:

    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - * /): ')
    num1Float = 0
    num2Float = 0

    numerosValidos = None

    try:
        num1Float = float(numero1)
        num2Float = float(numero2)
        numerosValidos = True
    except:
        numerosValidos = None

    if numerosValidos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadoresPermitidos = '+-*/'

    if operador not in operadoresPermitidos:
        print('Operador inválido!!!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando a sua operação. Confira o resultado abaixo: ')
    if operador == '+':
        resultado = num1Float + num2Float
    elif operador == '-':
        resultado = num1Float - num2Float
    elif operador == '*':
        resultado = num1Float * num2Float
    elif operador == '/':
        resultado = num1Float / num2Float
    else:
        print('Nunca deve chegar aqui')

    print(f'{num1Float} {operador} {num2Float} = {resultado}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair:
        break