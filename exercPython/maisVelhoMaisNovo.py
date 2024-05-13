age1 = int(input('Digite a idade da pessoa 1: '))
peso1 = int(input('Digite o peso da pessoa 1: '))
age2 = int(input('\nDigite a idade da pessoa 2: '))
peso2 = int(input('Digite o peso da pessoa 2: '))
if(age1==age2):
    print('\nVocês tem a mesma idade')
elif (age1>age2):
    print('\nPessoa 1 é mais velha, com ', age1, 'anos')
elif(age2>age1):
    print('\nPessoa 2 é mais velha com ', age2, 'anos')

if(peso1==peso2):
    print('\nVocês tem o mesmo peso')
elif (peso1>peso2):
    print('\nPessoa 1 é mais pesada, com ', peso1, 'kilos')
elif(peso2>peso1):
    print('\nPessoa 2 é mais pesada com ', peso2, 'kilos')