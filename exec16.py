# 16. Utilize uma lista para resolver o problema a seguir.
# Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas
# vendas brutas daquela semana. Por exemplo, um vendedor que
# teve vendas brutas de $3000 em uma semana recebe $200 mais
# 9 por cento de $3000, ou seja, um total de $470. Escreva
# um programa (usando um array de contadores) que determine
# quantos vendedores receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário,
# sem fazer vários ifs aninhados.


intervalos = [
    [200, 299], [300, 399], [400, 499],
    [500, 599], [600, 699], [700, 799],
    [800, 899], [900, 999]
    ]
quantidades = [0, 0, 0, 0, 0, 0, 0, 0, 0]

salarios = []

while True:
    vendas_brutas = float(input('Valor das vendas: '))
    continuma = input('Continua [S] ou [N]  ')

    if continuma in 'Nn':
        break
    else:
        salario = (vendas_brutas * 0.09) + 200
        if salario < 1000:
            for i in range(len(intervalos)):
                if salario > intervalos[i][0] and salario < intervalos[i][1]:
                    quantidades[i] += 1
        else:
            quantidades[8] += 1
print()
for i in range(len(intervalos)):
    print(f'Entre R$ {intervalos[i][0]} e R$ {intervalos[i][1]}: {quantidades[i]}')
print(f'Salarios maiores que R$1000: {quantidades[8]}')
