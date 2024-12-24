# dir, hasattr e getattr em Python

string = 'Dari'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper aqui!')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)