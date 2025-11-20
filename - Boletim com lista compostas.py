ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media]) # 'nome' = [0] // 'n1 e n2' = [1] // 'media' = [2]
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while c not in 'SN':
        print('Escolha entre [S/N], por favor...')
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print('-='*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>10}') # :<4 e <10 = 4 e 10 caracteres alinhados a esquerda // :>10 = 10 caracteres alinhados a direita
print('-='*30)
for i, a in enumerate(ficha): # Por indíce, aluno em enumerate
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') # 'i' = No // a[0] = Nome do aluno na posição 0 // # a[2] = Média do aluno na posição 2
while True:
    print('-='*30)
    aluno = int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno <= len(ficha) - 1: # O valor colocado na váriavel aluno, tem que ser menor que o número de alunos cadastrados em 'ficha'
        print(f'Notas de {ficha[aluno][0]} são: {ficha[aluno][1]}')
print('>>>>> VOLTE SEMPRE! <<<<<')
print('-='*30)