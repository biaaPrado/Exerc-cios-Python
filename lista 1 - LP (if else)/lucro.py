valor = float(input('Digite o valor da compra: '))
if valor < 20:
    print('Lucro de 45%: ', valor+(0.45*valor))
elif valor > 20:
    print('Lucro de 30%: ',valor+(0.30*valor))