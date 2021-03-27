# 8. Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade

idade = []
altura = []

for i in range(5):
    print(f'\nDADOS DA {i + 1}º PESSOA')
    idade.append(int(input('DIGITE A SUA IDADE:  ')))
    altura.append(float(input('DIGITE A SUA ALTURA:  ')))
print(f'IDADES: --> {idade}')
