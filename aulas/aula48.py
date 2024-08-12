'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de QUALQUER tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''
#        +01234
#        -54321
# string = 'ABCDE' # 5 caracteres
# print(bool(lista)) # falsy
# print(lista, type(lista))

#         0     1           2              3    4
#        -5    -4          -3             -2   -1
# lista = [123, True, 'Darieldon Medeiros', 1.2, []]

# lista[-3] = 'Rebeca Castro'
# print(lista[2].upper(), type(lista[2]))
# print(lista, type(lista))

#        0   1   2   3
lista = [10, 20, 30, 40]
# lista[2] = 300

# print(lista)
# del lista[2]

# print(lista)
# print(lista[2])

# lista.append(50)
# lista.pop() # remove o último elemento da lista
# lista.append(60)
# lista.append(70)

# ultimoValor = lista.pop(3)
# print(lista, 'Removido,', ultimoValor)
# É MAIS INTERESSANTE TRABALHAR COM OS VALORES AO FINAL DA LISTA (DEL)

# lista.append('Luiz')
# nome = lista.pop()

# lista.append(1233)
# del lista[-1]

# lista.clear()

# lista.insert(0, 5)
# lista.insert(1000000000, 'Darieldon') # Se o primeiro argumento ultrapassar o último índice da lista, o valor será colocado no último índice
# print(lista)

# listaA = [1, 2, 3]
# listaB = [4, 5, 6]
# listaC = listaA + listaB
# listaA.extend(listaB) # NÃO RETORNA VALOR, MEXE DIRETAMENTE NA PRIMEIRA LISTA (ANTES DO EXTEND)
# print(listaC)
# print(listaA)

'''
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''

nome = 'Darieldon'
outraVariavel = nome # o igual copiou o valor de nome para outraVariavel

nome = 'João'

print(nome)
print(outraVariavel)

listaA = ['Luiz', 'Maria', 1, True, 1.2]
listaB = listaA.copy() # Quando é para lista, ambas estão apontando para o mesmo local na memória, então se mudar em uma, na outra também muda

listaA[0] = 'Qualquer coisa'
print(listaA)
print(listaB)

