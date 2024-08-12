'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro
'''

numeroString = input('Digite um numero inteiro: ')

if numeroString.isdigit():
    numeroInt = int(numeroString)
    parImpar = numeroInt % 2 == 0
    parImparString = 'ímpar'

    if parImpar:
        parImparString = 'par'
    
    print(f'O número {numeroInt} é {parImparString}')
else:
    print('Você não digitou um número inteiro')

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11
Boa tarde 12-17
Boa noite 18-23
'''

horaString = input('Digite que horas são nesse momento: ')

try:
    horaInt = int(horaString)
    if horaInt >= 0 and horaInt <= 11:
        print('Bom dia!!!')
    elif horaInt >= 12 and horaInt <= 17:
        print('Boa tarde!!!')
    elif horaInt >= 18 and horaInt <= 23:
        print('Boa noite!!!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros!')


'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva  "Seu nome é normal"
maior que 6 escreve "Seu nome é muito grande
'''

nome = input('Digite o seu primeiro nome: ')
tamanhoNome = len(nome)

if tamanhoNome > 1:
    if tamanhoNome <= 4:
        print(f'Seu nome é curto, possui {tamanhoNome} letras')
    elif tamanhoNome >=5 and tamanhoNome <=6:
        print(f'Seu nome é normal, possui {tamanhoNome} letras')
    else:
        print(f'Seu nome é muito grande, possui {tamanhoNome} letras')
else:
    print('Digite mais de uma letra!')