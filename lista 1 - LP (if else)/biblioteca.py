nomeLivro = input('Digite o nome do livro: ')
user = input('Você é professor (P) ou aluno (A)? ')
prazo = 0

if user == 'P' or user == 'p':
    prazo = 10
    user = 'Professor'
elif user == 'A' or user == 'a':
    prazo = 3
    user = 'Aluno'

print('---------------------------------------')
print('\t\t\tRecibo de emprestimo')
print('Livro:', nomeLivro)
print('Usuário:', user)
print('Tempo:', prazo, 'dias')
print('---------------------------------------')


