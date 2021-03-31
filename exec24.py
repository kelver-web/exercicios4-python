# 24. Faça um programa que simule um lançamento de dados.
# Lance o dado 100 vezes e armazene os resultados em um vetor.
# Depois, mostre quantas vezes cada valor foi conseguido. Dica:
# use um vetor de contadores(1-6) e uma função para gerar numeros
# aleatórios, simulando os lançamentos dos dados.


from random import randint

lancamentos = []
dado = [1, 2, 3, 4, 5, 6]


def arremessos():
    for i in range(10):
        lancamentos.append(randint(1, 6))
    print('Números lançados!')
    print(lancamentos)

    for i in dado:
        print(f'O número {i} foi gerado {lancamentos.count(i)} vezes')


arremessos()
