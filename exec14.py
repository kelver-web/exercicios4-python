# 14. Utilizando listas faça um programa que faça 5 perguntas para
# uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma
# classificação sobre a participação da pessoa # no crime. Se a pessoa
# responder positivamente a 2 questões ela deve ser classificada como
# "Suspeita", entre 3 # e 4 como "Cúmplice" e 5 como "Assassino". Caso
# contrário, ele será classificado como "Inocente".

perguntas = ['Telefonou para a vitima? [s|n]: ',
             'Esteve no local do crime? [s|n]: ',
             'Mora perto da vitima? [s|n]: ',
             'Devia para a vitima? [s|n]: ',
             'Já trabalhou com a vítima? [s|n]: '
             ]

sim = 0

for i in range(len(perguntas)):
    resposta = input(perguntas[i])
    if resposta == 's':
        sim += 1
if sim == 2:
    print('Suspeita!')
elif sim > 2 and sim <= 4:
    print('Cumplice!')
elif sim == 5:
    print('Assassino!')
else:
    print('Inocente!')
