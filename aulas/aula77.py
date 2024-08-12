# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5x5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

iteracao = 0
resposta_certa = 0

for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}\n')
    print('Opções: ')

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')
    escolha = input('Escolha uma opção: ')
    
    
    if pergunta['Opções'][int(escolha)] == pergunta['Resposta']:
        print('Acertou! Parabéns! 👍\n')
        resposta_certa += 1
    
    else:
        print('Errou! ❌\n')
    iteracao += 1

print(f'Você acertou {resposta_certa} de {len(perguntas)} perguntas!')

0
# Imprime desse jeito:
'''
Pergunta: Quanto é 2+2?
Opções:
0) 1
1) 3
2) 4
3) 5
Escolha uma opção:

Se acertar: -> Acertou! Parabéns!
Se errar: -> Errou!
Vai incrementando um contador e no final mostra quantas acertou

'''

# Resposta do professor

# resposta_certa = 0
# for pergunta in perguntas:
#     print(f'Pergunta: {pergunta['Pergunta']}\n')
#     print('Opções: ')

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i}) {opcao}')

#     escolha = input('\nEscolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         resposta_certa += 1
#         print('Acertou! Parabéns! 👍\n')
#     else:
#         print('Errou ❌')

# print(f'Você acertou {resposta_certa} de {len(perguntas)} perguntas!')