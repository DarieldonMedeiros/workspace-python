'''
Iterando strings com while
'''
#       0123456789ABCDEF1011
nome = 'Darieldon Medeiros'
novaString = ''
asterisco = '*'
tamNome = len(nome)

contador = 0
while contador < tamNome:
    letra = nome[contador]
    novaString += f'*{letra}'
    contador += 1

novaString += '*'
print(novaString)
novaStringResposta = '*D*a*r*i*e*l*d*o*n* *M*e*d*e*i*r*o*s*'

print(novaString == novaStringResposta)

