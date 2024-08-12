'''
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
'''

def operacao (numero):
    def multiplicar(multiplicador):
        return numero * multiplicador
    return multiplicar

valor = 2
op = operacao(valor)

for mult in [2, 3, 4]:
    print(f'{valor} x {mult} = {op(mult)}')
