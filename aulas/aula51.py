'''
Introdução ao desempacotamento
'''

_, nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1, _)
# O * antes da variável pega o resto da lista
# Existe uma convenção de que *_ existe mas não será utilizada