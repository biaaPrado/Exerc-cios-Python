import math

x = int(input('Digite um valor para x: '))
numerador = (5*x + 3)
denominador = math.sqrt(x**2 - 16)

if (x**2 - 16) < 0:
    print('f(', x, ') não é real')
elif (x**2 - 16) == 0:
    print('f(', x, ') = infinito')
else:
    f = (numerador / denominador)
    print('f(', x, ') =', f)
