'''
Faça um jogo para o usuário adivinhar qual a palavra secreta
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra, você vai conferir se a letra digitada está na palavra secreta.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *
Faça a contagem de tentativas do seu usuário.
'''





















import os
tentativas = 1
palavraSecreta = 'Rebeca eu te amo!'
letraAcertada = ''
while True:
    if tentativas > 0:
        print(f'Estamos na {tentativas}° tentativa')
    
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra\n')
        tentativas += 1
        continue

    if len(letra) == 1:
        if letra.isdigit():
            print('Você digitou um número, repita o processo!\n')
            tentativas += 1
            continue
        else:
            if letra in palavraSecreta:
                letraAcertada += letra
            
            palavraFormada = ''
            for letraSecreta in palavraSecreta:
                if letraSecreta in letraAcertada:
                    palavraFormada += letraSecreta
                else:
                    palavraFormada += '*'
            
            print(f'Palavra formada: {palavraFormada}\n')
            if palavraFormada == palavraSecreta:
                break
            tentativas += 1

os.system('cls')
print('VOCÊ GANHOU, PARABÉNS!!!')
print(f'A palavra secreta era: {palavraSecreta}')
print(f'Tentativas: {tentativas}')