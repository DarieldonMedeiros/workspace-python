nome = 'Darieldon'
altura = 1.82
peso = 79

imc = peso / (altura ** 2)
variavel = ... # reticências é chamado de placeholder (onde não gera erro se a variável apresenta um número)
linha1 = f'{nome} tem {altura:.2f}m de altuura'
linha2 = f'pesa {peso} quilos e seu IMC é:'
linha3 = f'{imc:.2f}'
print(nome, ' tem ', altura, 'm de altura')
print('pesa', peso, 'kg e seu IMC é: ', imc)