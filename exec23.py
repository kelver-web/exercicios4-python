# 23. A ACME Inc., uma empresa de 500 funcionários, está tendo
# problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede
# precisa saber qual o espaço ocupado pelos usuários, e identificar
# os usuários com maior espaço ocupado. Através de um programa,
# baixado da Internet, ele conseguiu gerar o seguinte arquivo,
# chamado "usuarios.txt":
'''alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt",
no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados
em memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.'''


with open('usuarios.txt', encoding='cp1252') as arquivo:
    linhas = arquivo.read().splitlines()
    arquivo.close()


def nomes(lista):
    listaNome = []
    for i in range(len(lista)):
        listaNome.append(lista[i][0:14].rstrip())
    return listaNome


def tamanho_consumido(lista):
    listaConsumo = []
    for i in range(len(lista)):
        listaConsumo.append(int(lista[i][15:len(lista[i])]))
    return listaConsumo


def transforam_mega(lista):
    listaEmMega = []
    for i in range(len(lista)):
        listaEmMega.append(round(int(lista[i]) / 1048576, 2))
    return listaEmMega


def calcula_percentual(lista):
    percentuais = []
    valorTotal = sum(lista)
    for i in range(len(lista)):
        percentuais.append(round((lista[i] / valorTotal) * 100, 2))
    return percentuais


def cal_espaco_medio(lista):
    espacoMedio = round(sum(lista) / len(lista), 2)
    return espacoMedio


def relatorio(nomes, consumosMega, percentuais):
    if (len(nomes) == len(consumosMega) == len(percentuais)):
        open('relatorio.txt', 'a')
        arquivo = open('relatorio.txt', 'w')
        arquivo.write('ACME Inc.               Uso do espaco em disco pelos usuarios')
        arquivo.write(' ------------------------------------------------------------------ \n')
        arquivo.write('Nr.  Usuario        Espaco utilizado     % do uso\n')

        for i in range(len(nomes)):
            arquivo.write(f'{str(i + 1)}\
    {str(nomes[i])}\
        {str(consumosMega[i])}MB\
            {str(percentuais[i])}%\n')

        totalConsumo = sum(consumosMega)
        consumoMedio = cal_espaco_medio(consumosMega)
        arquivo.write(f'Consumo Total: {str(totalConsumo)}\
        \nConsumo Medio: {str(consumoMedio)}\n')
        arquivo.close()

    else:
        print('Quantidade de Usuarios e Dados Não Conferem.')


nomes = nomes(linhas)
consumos = tamanho_consumido(linhas)
consumosMega = transforam_mega(consumos)
percentuais = calcula_percentual(consumosMega)
relatorio(nomes, consumosMega, percentuais)
