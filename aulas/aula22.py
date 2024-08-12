'''
Operadores lógicos
and (e) or (ou) not (não)
or - Qualquer condição verdadeira avalia toda a expressão como verdadeira
Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliado naquele valor.
São considerados falsy (que você já viu)
0 0.0 '' False
Também existe o tipo None que é usado para representar um não valor (não existe)
'''

# entrada = input('[E]ntrar [S]air: ')
# senhaDigitada = input('Senha: ')

# senhaPermitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senhaDigitada == senhaPermitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
