# Desempacotamento em chamadas
# de métodos e funções
# O '*' serve para fazer o desempacotamento no print
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, c, *_, ap, u = lista
# print(p, u, ap)

salas = [
    #   0        1
    ['Maria', 'Helena', ],  # 0
    #   0
    ['Elaine', ],  # 1
    #   0      1         2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

print(*lista)
print(*string)
print(*tupla)

print(*salas, sep='\n')