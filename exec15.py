# 15. Faça um programa que leia um número indeterminado de valores,
# correspondentes a notas, encerrando a entrada de dados quando for
# informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados,
# um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;


notas = []
acima_media = []
baixa_media = []
nota = True
while nota != -1:
    nota = float(input("Digite a nota: "))
    if nota == -1:
        break
    else:
        notas.append(nota)
print(f'\nValores lidos: ------------> {len(notas)}')
print(f'Valores em ordem: ---------> {notas}')
print('valores decrescentes:')
notas.reverse()
for i in range(len(notas)):
    print(notas[i])
print(f'Soma dos valores: ---------> {sum(notas)}')
media = sum(notas) / len(notas)
print(f'Media dos valores: --------> {media:.2f}')

for i in range(len(notas)):
    if notas[i] > media:
        acima_media.append(notas[i])
print(f'valores a cima da media: --> {len(acima_media)}')
for i in range(len(notas)):
    if notas[i] < 7:
        baixa_media.append(notas[i])
print(f'notas a baixo de 7: -------> {len(baixa_media)}')
