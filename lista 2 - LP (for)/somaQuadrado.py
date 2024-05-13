soma = 0
lista_num = [2, 4, 6, 8, 10, 12, 14, 16, 19, 20]
for num in lista_num: #passa pelos numeros do array acima
    quad = num**2 #calcula o quadrado de cada numero
    print(quad)
    soma += quad #armazena a soma dos quadrados
print('Soma dos quadrados é =',soma)
