# 10. Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
# compostos pelos elementos intercalados dos dois outros vetores.

v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
juncao = []

for i in range(10):
    juncao.append(v1[i])
    juncao.append(v2[i])
print(juncao)
