# 19. Uma empresa de pesquisas precisa tabular os resultados da seguinte
# enquete feita a um grande quantidade de organizações:
'''Qual o melhor Sistema Operacional para uso em servidores?

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da
enquete e informe ao final o resultado da mesma. O programa deverá ler os
valores até ser informado o valor 0, que encerra a entrada dos dados. Não
deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os
valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular
a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a
40% dos votos.'''


print('QUAL O MELHOR SISTEMA OPERACIONAL PARA USO EM SERVIDORES?')
print('''1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro''')


votos = []
numero_votos = []
opcoes = ['Windowns Server', 'Unix', 'Linux', 'NetWare', 'MacOS', 'Outro']
n_voto = 1

while True:
    print(f'{n_voto}º Voto:')
    voto = int(input('Digite seu voto: '))
    if voto == 0:
        break
    else:
        while voto > 6 or voto < 1:
            print('Voto invalido!')
            print(f'{n_voto}º Voto:')
            voto = int(input('Digite o voto novamente: '))
        votos.append(voto)
    n_voto += 1

print_sistema = ('Sistema Operacional')
espaco1 = '      '
espaco2 = '   '
print_votos = 'Votos'
print()
print(print_sistema, espaco1, print_votos, ' ' * (len(espaco2) * 2), '%')
print('-' * len(print_sistema), espaco1, '-' * len(print_votos), espaco2, '-' * 7)
for i in range(len(opcoes)):
    numero_votos.append(votos.count(i + 1))
    print(opcoes[i], ' ' * (len(print_sistema) - len(opcoes[i]) + len(print_votos) + 3), votos.count(i + 1), ' ' * (len(espaco2) * 2), round(100 * votos.count(i + 1) / len(votos), 2), '%')
indice_ganhador = numero_votos.index(max(numero_votos))
print('\nO sistema mais votado foi o ', opcoes[indice_ganhador], ' com ', numero_votos[indice_ganhador], ' votos.')
print('Equivalente a ', round(100 * numero_votos[indice_ganhador] / len(votos), 2), '% dos votos.')