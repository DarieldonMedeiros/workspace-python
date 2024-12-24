# Generator expression, Iterables e Iterators em Python
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # tem __iter__ e __next__

# Iterator só conhece o próximo valor

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista)) # está na memória
print(sys.getsizeof(generator)) # não está na memória

for n in generator:
    print(n)