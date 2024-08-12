frase = 'O Python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido Van Rossun'

i = 0

maiorQuantidade = 0
letraApareceuMaisVezes = ''
while i < len(frase):
    letraAtual = frase[i]

    if letraAtual == ' ':
        i += 1
        continue

    qtdAtual = frase.count(letraAtual)


    if maiorQuantidade < qtdAtual:
        maiorQuantidade = qtdAtual

        letraApareceuMaisVezes = letraAtual


    print(letraAtual, qtdAtual)
    i += 1

print(f'A letra que apareceu mais vezes foi: "{letraApareceuMaisVezes}" em um total de {maiorQuantidade}x.')