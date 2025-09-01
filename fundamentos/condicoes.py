nota_aluno = float(input('Qual foi sua nota no exame? '))

if nota_aluno >= 7:
    print('Você foi aprovado!')
elif nota_aluno >= 5:
    print('Ficou de recuperação!')
else:
    print('Você foi reprovado!')
