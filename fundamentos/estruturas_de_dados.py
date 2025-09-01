tarefas = []
tarefas.append('Estudar Python')
tarefas.append('Ler um artigo sobre IA')
tarefas.append('Responder e-mails')

for tarefa in tarefas:
    print(f'Tarefa: {tarefa}')

meses = ('Jan', 'Fev', 'Mar')
print(meses)

pessoa = {
    'nome': 'Rafael',
    'idade': 18,
    'endereco': {
        'rua': 'Av. Brasil',
        'numero': 122
    }
}

print(pessoa['nome'])
print(pessoa['endereco']['rua'])