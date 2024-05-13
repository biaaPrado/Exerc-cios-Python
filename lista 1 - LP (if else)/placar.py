player1 = str(input('Nome do jogador 1: '))
score1 = int(input('Pontos do jogador 1:'))

player2 = str(input('\nNome do jogador 2: '))
score2 = int(input('Pontos do jogador 2:'))

player3 = str(input('\nNome do jogador 3: '))
score3 = int(input('Pontos do jogador 3:'))

if score1 > score2 > score3:
    print('Vencedor:\t', player1, '\t\t\t', score1, '\tpontos')
    print('Segundo colocado:\t', player2, '\t\t\t', score2, '\tpontos')
    print('Terceiro colocado:\t', player3, '\t\t\t', score3, '\tpontos')

elif score1 > score3 > score2:
    print('Vencedor:\t', player1, '\t\t\t', score1, 'pontos')
    print('Segundo colocado:\t', player3, '\t\t\t', score3, '\tpontos')
    print('Terceiro colocado:\t', player2, '\t\t\t', score2, '\tpontos')

elif score2 > score1 > score3:
    print('Vencedor:\t', player2, '\t\t\t', score2, '\tpontos')
    print('Segundo colocado:\t', player1, '\t\t\t', score1, '\tpontos')
    print('Terceiro colocado:\t', player3, '\t\t\t', score3, '\tpontos')

elif score2 > score3 > score1:
    print('Vencedor:\t', player2, '\t\t\t', score2, '\tpontos')
    print('Segundo colocado:\t', player3, '\t\t\t', score3, '\tpontos')
    print('Terceiro colocado:\t', player1, '\t\t\t', score1, '\tpontos')

elif score3 > score2 > score1:
    print('Vencedor:\t', player3, '\t\t\t', score3, '\tpontos')
    print('Segundo colocado:\t', player2, '\t\t\t', score2, '\tpontos')
    print('Terceiro colocado:\t', player1, '\t\t\t', score1, '\tpontos')

elif score3 > score1 > score2:
    print('Vencedor:\t', player3, '\t\t\t', score3, '\tpontos')
    print('Segundo colocado:\t', player1, '\t\t\t', score1, '\tpontos')
    print('Terceiro colocado:\t', player2, '\t\t\t', score2, '\tpontos')

