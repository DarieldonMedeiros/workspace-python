'''
    1. (n + n) -> primeiro executa os parênteses
    2. ** -> depois vem a exponenciação
    3. * / // % -> depois vem multiplicação, divisão, divisão inteira e módulo
    4. + - -> e por último vem a adição e subtração
'''
conta1 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1024
print(conta1)