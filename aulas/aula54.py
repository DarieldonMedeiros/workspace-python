"""
Faça uma lista de ocmprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.

TEXTO INICIAL:
Selecione uma opção
[i]nserir [a]pagar [l]istar:


l -> Se lista = vazia: Nada para listar, caso contrário, mostra a lista de itens
a -> Se lista = vazia ou índice inexistente: não foi possível apagar este índice e volta para o TEXTO INICIAL, caso contrário, apaga o item desejado
i -> pergunta o "Valor: " e adiciona a lista


"""
import os
lista = []

while True:
    opcao = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ")

    if opcao == "i":
        os.system('cls')
        valor = input("Valor: ")
        lista.append(valor)
        
    elif opcao == "l":
        os.system('cls')
        if len(lista) == 0:
            print("Nada para listar")
        else:
            for indice, nome in enumerate(lista):
                print(indice, nome)

    elif opcao == "a":
        os.system('cls')
        if len(lista) == 0:
            print("A lista está vazia, não há nada para apagar")
        else:
            indiceSTR = input("Digite o índice a ser apagado: ")
            try:
                indice = int(indiceSTR)
                del lista[indice]
                print(f'Índice {indiceSTR} apagado com sucesso')
            except ValueError:
                print('Por favor digite um número inteiro')
            except IndexError:
                print('Índice não existe na lista')
            except Exception as erro:
                print(f'Ocorreu um erro inesperado: {erro}')

            
    else:
        print('Por favor, escolha i, a ou l')