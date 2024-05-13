import math
num = int(input('Digite um numero:'))

if num > 0:
    #print('A raiz quadrada de', num, 'é', num**(1/2))
    print('A raiz quadrada de', num, 'é', math.sqrt(num))
elif num < 0:
    print('O quadrado de', num, 'é', num**2)