n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))

media = ((n1+n2+n3) / 3)
print(media)

if (media >= 0) and (media < 5):
    print('reprovado')
elif (media >= 5) and (media < 6):
    print('reuperação')
elif media >= 6:
    print('aprovado')
elif media < 0 or media > 10:
    print('valor inválido')

