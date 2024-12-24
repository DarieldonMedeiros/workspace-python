
# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno

# Criando um set
# set(iterável) ou {1, 2, 3}
s1 = set(('Darieldon', 1, 2, 3))
s1 = {'Darieldon', 1, 2, 3}
print(s1) # Não garante ordem

# Sets são eficientes para remover valores duplicados de iteráveis.
#   - Não aceitam valores mutáveis;
#   - Seus valores serão sempre únicos;
#   - Não tem índexes;
#   - Não garantem ordem;
#   - São iteráveis (for, in, not in)

l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = { 1, 2, 3, 3, 3, 3, 3, 1} # elimina automaticamente valores repetidos
s2 = set(l1)
l2 = list(s2)
s3 = {1, 2, 3, (123,)}
print(s3)

print(3 in s3)

for numero in s3:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

s4 = set()
s4.add('Darieldon')
s4.add(1)
s4.update(('Olá mundo', 1, 2, 3, 4))
s4.discard('Olá mundo')
print(s4)

# Operadores úteis
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda

s5 = {1, 2, 3}
s6 = {2, 3, 4}
s7 = s5 | s6 # ou
s8 = s5 & s6 # e
s9 = s5 - s6 # mostra os únicos da esquerda (s5)
s10 = s6 - s5 # mostra os únicos da esquerda (s6)
s11 = s6 ^ s5 # mostra os elementos únicos totais (seria )
print(f's7 = {s7}')
print(f's8 = {s8}')
print(f's9 = {s9}')
print(f's10 = {s10}')
print(f's11 = {s11}')