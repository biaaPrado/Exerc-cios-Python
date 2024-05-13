nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))

if idade <= 10:
    print('O valor a ser pago por', nome, 'é de 30 reais')
elif 10 < idade < 29:
    print('O valor a ser pago por', nome, 'é de 60 reais')
elif 29 < idade < 45:
    print('O valor a ser pago por', nome, 'é de 120 reais')
elif 45 < idade < 59:
    print('O valor a ser pago por', nome, 'é de 150 reais')
elif 59 < idade < 65:
    print('O valor a ser pago por', nome, 'é de 250 reais')
elif idade >= 65:
    print('O valor a ser pago por', nome, 'é de 400 reais')