'''
Tipo tupla - Uma lista imutável
Para criar uma tupla tem alguns métodos, dentre eles:
    * Não colocar colchetes "[]"
    * Colocar parênteses "()"
'''
nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
nomes = list(nomes)
print(nomes[0])
print(nomes[-1])
print(nomes)
# O * antes da variável pega o resto da lista
# Existe uma convenção de que *_ existe mas não será utilizada