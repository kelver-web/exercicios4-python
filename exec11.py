# 11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
v3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

juncao = []

for i in range(10):
    juncao.append(v1[i])
    juncao.append(v2[i])
    juncao.append(v3[i])
print(juncao)