'''
enumerate - enumera iteráveis (índices)
'''
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# listaEnumerada = list(enumerate(lista))

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for tuplaEnumerada in enumerate(lista):
#     indice, nome = tuplaEnumerada
#     print(indice, nome)


# for tuplaEnumerada in enumerate(lista):
#     print('FOR da tupla: ')
#     for valor in tuplaEnumerada:
#         print(f'\t{valor}')

# print('O que tem na lista enumerada:', listaEnumerada)


# O enumerate consome os valores quando os elementos são impressos (para o ponteiro no final da lista)
# O segredo é não declarar o enumerate em uma variável
