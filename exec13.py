# 13. Faça um programa que receba a temperatura média de cada mês
# do ano e armazene-as em uma lista. Após isto, calcule a média
# anual das temperaturas e mostre todas as temperaturas acima da
# média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio',
         'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro'
         ]

lista_temp = []
altas_temps = []
meses_altas = []
juncao = []

for i in meses:
    print(f'\nTEMPERATURA DO MÊS DE --> {i}:'.title())
    lista_temp.append(float(input('Temp C°:  ')))

    media_anual = sum(lista_temp) / len(lista_temp)

for i in range(len(lista_temp)):
    if lista_temp[i] > media_anual:
        altas_temps.append(lista_temp[i])
        meses_altas.append(meses[i])

        juncao.append(meses_altas[i])
        juncao.append(altas_temps[i])

print()
print(f'TEMP. MÉDIA DO ANO -----------> {media_anual:.2f} C°')
print(f'TEMPS ACIMA DA MÉDIA DO ANO --> {altas_temps} C°')
print()
print('MESES DE TEMP. MAIS ALTA:')
for i in juncao:
    print(i)
