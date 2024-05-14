n = 0
b = 0
while n <= 1 and b <= 2: #enquanto o valor de n e b não satisfazer a condição vai repetir
    n = int(input('Receba o valor de n: '))
    b = int(input('Receba o valor de b: '))
    if n <= 1 and b <= 2:
        print('Valores inválidos para N e B\n')
print('\nO valor de b^n = ', b**n)