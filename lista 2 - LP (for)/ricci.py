n = 0
while n <= 1:
    n = int(input('Informe o numero de termos: '))
    if n <= 1:
        print('Valor inválido, redigite')
a = int(input('Informe o termo 1: '))
b = int(input('Informe o termo 2: '))

print('-----RICCI------')
print('| Termo 1 :', a, '\t|')
print('| Termo 2 :', b, '\t|')
for num in range(3, n+1):
    c = a + b
    a = b
    b = c
    print('| Termo', num, ':', c, '\t|')
print('----------------')
