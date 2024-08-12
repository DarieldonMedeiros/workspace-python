'''
Operadores lógicos
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
São considerados falsy (que você já viu)
0 0.0 '' False
Também existe o tipo None que é usado para representar um não valor (não existe)
'''

# entrada = input('[E]ntrar [S]air: ')
# senhaDigitada = input('senha: ')

# senhaPermitida = '123456'

# if entrada == 'E' and senhaDigitada == senhaPermitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print( True and 0 and True)
print(bool(''))

if 1 and 1:
    print(True and 1 and False)