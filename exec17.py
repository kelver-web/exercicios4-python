# 17. Em uma competição de salto em distância cada atleta tem direito
# a cinco saltos. O resultado do atleta será determinado pela média
# dos cinco valores restantes. Você deve fazer um programa que receba
# o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
# e depois informe o nome, os saltos e a média dos saltos. O programa
# deve ser encerrado quando não for informado o nome do atleta.
# A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

ordem_salto = ['primeiro', 'segundo', 'terceiro',
               'quarto', 'quinto']

saltos = []
nome_atleta = True
n_atleta = 1

while nome_atleta != '':
    nome_atleta = input('\nATLETA:  ')
    n_atleta += 1
    print()

    if nome_atleta == '':
        break

    else:
        for i in ordem_salto:
            distancia = float(input(f'{i} Salto:  '))
            saltos.append(distancia)
        print()
        print('Resultado final:')
        print(f'Atleta: {nome_atleta}')
        print(f'Saltos: {saltos}')
        print(f'Média dos saltos: {sum(saltos) / len(saltos):.2f} m')
