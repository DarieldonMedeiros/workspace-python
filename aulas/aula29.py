'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar o código
'''

numeroStr = input('Vou dobrar o número que você digitar: ')
# if numeroStr.isdigit():
#     numeroFloat = float(numeroStr)
#     print(f'O dobro de {numeroStr} é {numeroFloat * 2:.0f}')
# else:
#     print('Isso não é um número')

try:
    print('STR: ', numeroStr)
    numeroFloat = float(numeroStr)
    print('FLOAT: ', numeroFloat)
    print(f'O dobro de {numeroStr} é {numeroFloat * 2:.0f}')
except:
    print('Isso não é um número')