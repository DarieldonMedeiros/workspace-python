'''
Closure e funções que retornam outras funções

Closure é uma característica do Python que permite que funções armazenem o estado de outras funções, mesmo depois de ambas as funções terem sido destruídas.
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom noite')


for nome in ['Darieldon', 'Rebeca', 'Harry']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))