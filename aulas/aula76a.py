'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''
import copy

pessoa = {
    'nome': 'Darieldon',
    'sobrenome': 'de Brito Medeiros 1',
    'sobrenome': 'de Brito Medeiros', 
    'idade': 29,
}
# se colocar uma chave igual na declaração do dicionário, somente o último valor será válido
pessoa.setdefault('idade', None)
print(pessoa['idade'])

print(len(pessoa))
print(tuple(pessoa.keys())) # variavel.keys() -> pode ser transformado em tupla

for chave in pessoa.keys():
    print(chave)

print(list(pessoa.values()))

for chave, valor in pessoa.items():
    print(chave, valor)


d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2], # Listas são copiadas via cópia rasa
}

d2 =  copy.deepcopy(d1) # por padrão faz uma cópia rasa
# deepcopy faz uma cópia profunda
d2['c1'] = 1000
d2['l1'][1] = 999999 # altera também no d1
print(d1)
print(d2)

# Métodos get, pop, update

p1 = {
    'nome': 'Darieldon',
    'sobrenome': 'de Brito Medeiros',
}

# print(p1['nome'])
print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# sobrenome = p1.popitem()
# print(sobrenome)
# print(p1)
# p1.update({
#     'nome': 'Rebeca',
#     'idade': 27,
# })
# print(p1)

# p1.update(nome='Rebeca', idade=27)
# print(p1)

tupla = ('nome', 'Rebeca'), ('idade', 27)
lista = [['nome', 'Rebeca'], ['idade', 27]]
p1.update(lista)
print(p1)
