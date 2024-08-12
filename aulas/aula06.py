# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# string, int, float, bool (tipos imutáveis)
print(1 + 1)
print('a' + 'b') # polimorfismo -> o mesmo sinal faz 2 operações diferentes
# print('1' + 1) #-> não dá para concatenar 2 tipos diferentes (linguagem com tipagem forte)
print(int('1'), type(int('1')))
print(float('1') + 1)
print(bool(' '))
print(str(11) + 'b')