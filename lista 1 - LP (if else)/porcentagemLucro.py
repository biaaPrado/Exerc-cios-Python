prod = input('Digite o nome do produto: ')
valor = int(input('Digite o valor de compra: '))
valorVenda= 0
lucro = 0

if valor < 10:
    valorVenda = valor + (0.7*valor)
    lucro = '70%'
elif 10 <= valor < 30:
    valorVenda = valor + (0.5*valor)
    lucro =  '50%'
elif 30 <= valor < 50:
    valorVenda = valor + (0.4 * valor)
    lucro = '40%'
elif valor >= 50:
    valorVenda = valor + (0.3 * valor)
    lucro = '30%'
print('\nValor de venda para', prod, 'será de R$', valorVenda, '(lucro de',lucro, ')')