n = int(input('Informe a quantidade de termos: '))
soma = 0

for c in range(1, n+1):
    termo = 1/c
    soma += termo
    print('Termo (', c, ') =', termo)
print('\nSomatória: ', soma)
