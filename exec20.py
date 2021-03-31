# 20. As Organizações Tabajara resolveram dar um abono aos
# seus colaboradores em reconhecimento ao bom resultado alcançado
# durante o ano que passou. Para isto contratou você para desenvolver
# a aplicação que servirá como uma projeção de quanto será gasto com o
# pagamento deste abono.
'''Após reuniões envolvendo a diretoria executiva, a diretoria financeira
e os representantes do sindicato laboral, chegou-se a seguinte forma
de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de
dezembro;
a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário
for
muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma
preocupação com colaboradores com tempo menor de casa, descontos, impostos ou
outras
particularidades. Seu programa deverá permitir a digitação do salário de um
númeroindefinido (desconhecido) de salários. Um valor de salário igual a 0
(zero) encerra a digitação. Após a entrada de todos os dados o programa deverá
calcular o valor do abono concedido a cada colaborador, de acordo com a regra
definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do
programa,
apenas para fins ilustrativos. Os valores podem mudar a cada execução do
programa.
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0

Salário    - Abono
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00'''


salarios = []
abonos = []
salario = True
n_funcionario = 1
print('Digite [0] para sair')
while salario != 0:
    print(f'\n{n_funcionario}º Funcionário:')
    n_funcionario += 1
    salario = float(input('Digite o salario: '))
    if salario == 0:
        break
    else:
        while salario < 0:
            print('Salário inválido!')
            print(f'\n{n_funcionario}º Funcionário:')     
            salario = float(input('Digite novamente: '))
        abonos.append(salario * 0.2)
        salarios.append(salario)
print()
print('Projeção de Gastos com Abono')
print('=============================')
valor_minimo = 0
for i in range(len(salarios)):
    if abonos[i] <= 100:
        print(f'Salario = R$ {salarios[i]} - Abono = R$ 100.0')
        abonos[i] = 100
        valor_minimo += 1
        continue

    print(f'Salários: {salarios[i]:.2f}')
print()
espaco1 = '   '
sala = ('Salário')
abono = ('Abono')
print(sala, espaco1, abono)

for i in range(len(salarios)):
    print(f'R$ {salarios[i]:.2f} - R$ {abonos[i]:.2f}')

print(f'\nForam processados {len(salarios)} colaboradores.')
print(f'Total gasto com abonos: R$ {sum(abonos):.2f}')
print(f'Valor minimo pago a {valor_minimo} colaboradores.')
print(f'Maior valor de abono pago: {max(abonos):.2f}')
