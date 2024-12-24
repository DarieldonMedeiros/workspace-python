# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Rebeca',
    'sobrenome': 'Castro',
}

dados_pessoa = {
    'idade': 27,
    'altura': 1.7
}

# utiliza 2 asteriscos (**) para extrair todos os dados de um dicionário
pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)
# # entrega somente as chaves
# a, b = pessoa
# print(a, b)

# # entrega os valores de cada chave
# c, d = pessoa.values()
# print(c, d)

# # entrega uma tupla com a key e o valor
# e, f = pessoa.items()
# print(e, f)

# # desempacotamento interno

# (g1, g2), (h1, h2) = pessoa.items()
# print(g1, g2)
# print(h1, h2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

# kwargs - vem precedido de 2 asteríscos em funções
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS', args) # argumentos não nomeados

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(1, 2, 3, nome = 'Rebeca', qlq = 123)

mostro_argumentos_nomeados(**pessoa_completa) # desempacota uma chamada de argumentos

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
    'arg5': 5,
    'arg6': 6,
    'arg7': 7,
    'arg8': 8,
    'arg9': 9,
    'arg10': 10,
    'arg11': 11,
}

mostro_argumentos_nomeados(**configuracoes)