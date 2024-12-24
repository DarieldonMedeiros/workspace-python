'''
Exercício
Crie uma função (def) que encontra o primeiro duplicado considerando o segundo número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
    Se não encontrar duplicados na lista, retorne -1

'''

def encontra_duplicada(lista):
    indices = range(len(lista))
    primeiro_duplicado = -1
    set_lista = set()
    tamanho_set = 0
    for i in indices:
        set_lista.add(lista[i])
        tamanho_set += 1
        if len(set_lista) != tamanho_set:
            primeiro_duplicado = lista[i]
            return f'O primeiro número repetido da lista {lista} é o : {primeiro_duplicado}'
    return f'Não há números repetidos na lista {lista}, logo retorna {primeiro_duplicado}'


lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # não repete (-1)
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8], # repete (9)
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7], # repete (2)
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9], # repete (8)
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],# repete (8)
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9], # repete (2)
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1], # repete (2)
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3], # repete (1)
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7], # repete (1)
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1], # repete (2)
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7], # repete (5)
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], # não repete (-1)
]

indices_da_lista = range(len(lista_de_listas_de_inteiros))

for indice in indices_da_lista:
    print(encontra_duplicada(lista_de_listas_de_inteiros[indice]))


# Resposta do professor

# def encontra_primeiro_duplicado(lista_de_inteiros):
#     numeros_checados = set()
#     primeiro_duplicado = -1
#     for numero in lista_de_inteiros:
#         if numero in numeros_checados:
#             primeiro_duplicado = numero
#             break
#         numeros_checados.add(numero)
    
#     return primeiro_duplicado


# for lista in lista_de_listas_de_inteiros
#     print(lista)