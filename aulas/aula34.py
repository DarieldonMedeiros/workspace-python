'''
Repetições
while (enquanto)
Executa ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''

condicao = True

while condicao:
    nome = input('Qual é o seu nome? ')
    
    if nome == 'sair':
        print('Obrigado por usar o programa!')
        break
    else:
        print(f'O seu nome é {nome}')

print('Acabou')