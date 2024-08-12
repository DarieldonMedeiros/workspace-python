'''
split e join com list e str
spit -> divide uma string
join -> une uma string (com outras strings)

strip -> retira os espaços no começo e no final
rstrip -> retira os espaços da direita
lstrip -> retira os espaços da esquerda
'''
frase = '   Olha só que    ,    coisa interessante     '
lista_frases_cruas = frase.split(',') # o argumento do split pode ser definido dentro da função


lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
