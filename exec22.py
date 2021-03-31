# 22. Sua organização acaba de contratar um estagiário para trabalhar
# no Suporte de Informática, com a intenção de fazer um levantamento
# nas sucatas encontradas nesta área. A primeira tarefa dele é testar
# todos os cerca de 200 mouses que se encontram lá, testando e anotando
# o estado de cada um deles, para verificar o que se pode aproveitar deles.
'''Foi requisitado que você desenvolva um programa para registrar este
levantamento. O programa deverá receber um número indeterminado de entradas,
cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou
inutilizado Uma identificação igual a zero encerra o programa. Ao final o
programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%'''


print('''==== SISTEMA DE IDENTIFICAÇÃO DE MANUTENÇÃO DE MOUSES ===
[1] NECESSITA DA ESFERA
[2] NECESSITA DE LIMPEZA
[3] NECESITA TROCA DO CABO/CONECTOR
[4] QUEBRADO/INUTILIZADO''')


defeitos = ['necessita da esfera                    ',
            'necessita de limpeza                   ',
            'necessita troca do cabo ou conector    ',
            'quebrado ou inutilizado                '
            ]

n_idantifacao = []
n_defeito = []
identificacao = True
n_mouse = 1
print('Digite [0] para sair!')
while identificacao != 0:
    print(f'\n{n_mouse}º Mouse:')
    identificacao = int(input('Nº De Identificação do mouse: '))
    if identificacao == 0:
        break
    else:
        while identificacao in n_idantifacao:
            print(' == Número já existente ==')
            print(f'\n{n_mouse}º Mouse:')
            identificacao = int(input('Nº De Identificação do mouse: '))
        numero_defeito = int(input('Nº do defeito: '))
        while numero_defeito > 4 or numero_defeito < 1:
            print('== Número inexistente! ==')
            numero_defeito = int(input('Nº do defeito: '))
        n_idantifacao.append(identificacao)
        n_defeito.append(numero_defeito)
    n_mouse += 1
print("\nQuantidade de mouses: ", len(n_idantifacao))
espaco1 = '                               '
espaco2 = '  '
print('SITUAÇÃO', espaco1, 'QUANTIDADE', espaco2, '  PERCENTUAL')
for i in range(len(defeitos)):
    print(f'{i + 1} - {defeitos[i]}\
    {n_defeito.count(i + 1):.2f}\
        {100 * n_defeito.count(i + 1) / len(n_idantifacao):.2f} %')

