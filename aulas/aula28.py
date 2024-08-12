'''
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido = {nomeInvertido}
        SeU nome contém (ou não espaços)
        Seu nome tem {n} letras
        A primeira letra do seu nome é {Primeira}
        A última letra do seu nome é {Última}
Se nada for digitado em nome ou idade:
    Exiba: "DESCULPE, VOCÊ DEIXOU CAMPOS VAZIOS"
'''

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
tamanhoNome = len(nome)
print(30* '-')
if not nome or not idade:
    print('Desculpe, você deixou campos vazios')
else:
    print(f'Seu nome é: {nome}!')
    print(f'Seu nome invertido é: {nome[::-1]}!')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contém espaços')
    print(f'O seu nome tem {tamanhoNome} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[tamanhoNome-1]}')