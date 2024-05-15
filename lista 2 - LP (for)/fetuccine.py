x = int(input('Digite o primeiro termo: '))
y = int(input('Digite o segundo termo: '))

print('Termo 1 :', x)
print('Termo 2 :', y)

for n in range(3,10):
    termo = y #termo atual sera o ultimo q foi informado pelo user
    if n % 2 == 0: #saber se o termo é par ou impar e respeitar sua formula
        y = y - x
    else:
        y = y + x
    x = termo
    print('Termo', n, ':', y)