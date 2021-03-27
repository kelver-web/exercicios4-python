# 12. Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com
# mais de 13 anos possuem altura inferior à média de
# altura desses alunos.


alturas = []
idades = []
alunos_de13 = []
media_baixa = []

for i in range(10):
    print(f'\n{i + 1}º ALUNO:  ')
    alturas.append(float(input('ALTURA:  ')))
    idade = int(input('IDADE:  '))
    if idade > 13:
        alunos_de13.append(idade)
    idades.append(idade)

media = sum(alturas) / len(alturas)

for i in range(len(alunos_de13)):
    if alunos_de13[i] < media:
        media_baixa.append(alunos_de13[i])

print(f'MÉDIA DE ALTURA: {media:.2f}')
print(f'ALUNOS COM MAIS DE 13 ANOS ABAIXO DA MÉDIA DE ALTURA = {len(str(media_baixa))}')
