# 6. Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno, imprima
# o número de alunos com média maior ou igual a 7.0.

media7 = []

for i in range(5):
    notas = []
    print(f'\n{i + 1}º ALUNO:')
    for i in range(4):
        notas.append(float(input(f'DIGITE A {i + 1}º NOTA:  ')))

    media = (sum(notas) / len(notas))

    if media >= 7:
        media7.append(media)
print()
print(f'ALUNOS COM MÉDIA 7 OU SUPERIOR = {len(media7)}')
