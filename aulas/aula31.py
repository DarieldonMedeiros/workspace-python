'''
Flag (Bandeira) - Marcar um logal
None = Não valor
is e is not  = é ou não é (tipo, valor, identidade)
id = identidade

'''

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

condicao = False
passouNoIf = None

if condicao:
    passouNoIf = False
    print ('Faça algo')
else:
    print('Não faça algo')

print(passouNoIf, passouNoIf is None)
print(passouNoIf, passouNoIf is not None)

if passouNoIf is None:
    print('Não passou no if')

if passouNoIf is not None:
    print('Passou no if')
