'''
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
'''

import decimal # somente para números de pontos flutuantes com muitas casas decimais (se colocar uma string resolve o problema)
numero1 = decimal.Decimal('0.1')
numero2 = decimal.Decimal('0.7')
numero3 = numero1 + numero2

print(numero3)
print(f'{numero3:.2f}') # formatar o resultado final é uma das formas de contornar -> retorna uma string
print(round(numero3, 2)) # round arredonda o número -> retorna um float. Se colocar mais casas decimais, mostra até a última casa decimal
