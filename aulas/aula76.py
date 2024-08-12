'''
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo par de "chave" e "valor"
Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipos imutáveis como str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
pessoa = {
    'nome': 'Darieldon',
    'sobrenome': 'de Brito Medeiros',
    'idade': 29,
    'altura': 1.8,
    'endereços': [
        {'rua': 'Rua João Damasceno', 'número': 155}
        {'rua': 'Rua João Damasceno', 'número': 216}
    ]
}
print(pessoa, type(pessoa))
'''
# pessoa_1 = dict(nome='Darieldon', sobrenome='de Brito Medeiros')

# manipulando chaves e valores em dicionários
pessoa = {
    'nome': 'Darieldon',
    'sobrenome': 'de Brito Medeiros',
    'idade': 29,
    'altura': 1.8,
    'endereços': [
        {'rua': 'Rua João Damasceno', 'número': 155},
        {'rua': 'Rua João Damasceno', 'número': 216},
    ]
}
# print(pessoa, type(pessoa))

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

print()

pessoa_1 = {}

##
##
chave = 'nome'
pessoa_1[chave] = 'Rebeca Castro'
pessoa_1['sobrenome'] = 'Santiago'

print(pessoa_1[chave])

pessoa_1[chave] = 'Harry'
del pessoa_1['sobrenome']
print(pessoa_1)
print(pessoa_1['nome'])

if pessoa_1.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa_1['sobrenome'])


# Esta aula mostra o processo de CRUD (Create, Read, Update and Delete)!