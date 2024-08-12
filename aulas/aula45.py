'''
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''
texto = 'Darieldon' #iterável
iterador = iter(texto) #iterador

# O laço for faz isso debaixo dos panos
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
