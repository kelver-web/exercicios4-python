# 4. Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. Imprima as consoantes.

consoantes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
vogais = ['a', 'e', 'i', 'o', 'u']
count = 0
while count < 5:
    if vogais[count] in consoantes:
        consoantes.remove(vogais[count])
    count += 1
print(f'EXISTEM {len(consoantes)} CONSOANTES')
print(f'SÃO: {consoantes}')
