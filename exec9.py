# 9. Faça um Programa que leia um vetor A com 10 números inteiros,
# calcule e mostre a soma dos quadrados dos elementos do vetor.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = []

for i in range(len(a)):
    quadrados.append(a[i] * a[i])
    i += 1
print(f'SOMA DOS QUADRADOS: --> {sum(quadrados)}')
