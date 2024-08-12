a = 'A'
b = 'B'
c = 1.1
string = 'b={1} a={0} a={0}  a={0} c={nome3:.2f}' # Tudo começa no índice zero

formato = string.format(
    a, b, nome3 = c
)

print(formato)

nome = 'Luiz'
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n = nome, i = idade))

formato = f'{nome} tem {idade:.2f} anos'
print(formato)

