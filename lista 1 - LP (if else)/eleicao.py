municipio = str(input('Digite o nome do município: '))
eleitores = int(input('Digite a quantidade de eleitores: '))

if eleitores > 20000:
    votos = int(input('Total de votos do primeiro colocado: '))
    if votos < (0.5 * eleitores):
        print('O município de', municipio, 'terá segundo turno')
    else:
        print('O município de', municipio, 'não terá segundo turno')
elif eleitores < 20000:
    print('O município de', municipio, 'não terá segundo turno')