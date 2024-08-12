'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
'''
x = 1 # x definido fora da função

def escopo():
    global x # se definir como global, altera fora da função também
    x = 10 # x definido dentro da função
    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

print(x) # a alteração dentro da função altera somente naquele escopo
escopo()
print(x) # a alteração dentro da função altera somente naquele escopo