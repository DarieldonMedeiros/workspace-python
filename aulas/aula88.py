# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis (), "", 0 0.0 None False range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nenhum = None
falso = False
intervalo = range(0)

variaveis_falsas = ['TESTE', lista, dicionario, conjunto, tupla, string, inteiro, flutuante, nenhum, falso, intervalo]

def falsy(valor):
    return 'Falsy' if not valor else 'Truthy'

def nome_variavel(var):
    for name, value in globals().items():
        if value is var:
            return name

for item in variaveis_falsas:
    print(f'{nome_variavel(item)} =', falsy(item))