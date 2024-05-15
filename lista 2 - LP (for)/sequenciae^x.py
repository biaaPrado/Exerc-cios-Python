import math

x = int(input('Informe o valor de x: '))
soma = 0

for n in range(0, 10):
    termo = (x**n)/math.factorial(n)
    soma += termo
    print('Termo (', n, ') = ', termo)
print('\nSomatório de e**x: ', soma)