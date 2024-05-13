saldoMedio = float(input('Digite o valor do saldo médio: '))
credito = 0

if 0 <= saldoMedio <= 500:
    print('\nNenhum crédito adicional')
elif 500 < saldoMedio <= 1000:
    credito = saldoMedio * 0.3
elif 1000 < saldoMedio <= 3000:
    credito = saldoMedio * 0.4
elif saldoMedio > 3000:
    credito = saldoMedio * 0.5

print('\nValor do saldo:', saldoMedio)
print('Crédito adicional de R$', credito)