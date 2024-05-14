temp_ini = int(input('Temperatura inicial da tabela (em Celcius): '))
temp_fim = int(input('Temperatura final da tabela (em Celcius): '))
temp_fah = 0
print('CELCIUS\t\tFAHRENHEIT')
for temp in range(temp_ini, temp_fim+1):
    temp_fah = temp*1.8 + 32
    print(temp, '\t\t\t', round(temp_fah, 1)) #round formata o n de casas decimais