# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    # yield 1 # Pausar
    # print('Continuando...')
    # yield 2 # Pausar
    # print('Mais uma vez...')
    # yield 3 # Pausar
    # print('Vou terminar')
    # return 'ACABOU'
    while True:
        yield n
        n += 1

        if n >= maximum:
            return
# TODA GENERATOR FUNCTION POSSUI O YIELD

gen = generator(maximum = 100000)
for n in gen:
    print(n)