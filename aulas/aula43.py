# senhaSalva = '123456'
# senhaDigitada = ''
# repeticoes = 0

# while senhaDigitada != senhaSalva:
#     senhaDigitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(f'O número total de repetições foram {repeticoes}x')
# print('Aquele laço acima pode ter repetições infinitas')

texto = 'Python'

novoTexto = ''
for letra in texto:
    novoTexto += f'*{letra}'
    print(letra)

print(novoTexto + '*')