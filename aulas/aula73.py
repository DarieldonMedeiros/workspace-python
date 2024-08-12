'''
High Order Functions
Funções de primeira de primeira classe

High Order Functions: Funções que podem receber e/ou retornar outras funções
First-Class Functions: Funções que são tratadas com outros tipos de dados comuns(strings, inteiros, etc.)
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Bom dia', 'Darieldon')
print(v)

v = executa(saudacao, 'Boa noite', 'Rebeca')
print(v)