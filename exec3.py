# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

n1 = float(input('DIGITE 1º NOTA:  '))
n2 = float(input('DIGITE 2º NOTA:  '))
n3 = float(input('DIGITE 3º NOTA:  '))
n4 = float(input('DIGITE 4º NOTA:  '))
notas = n1, n2, n3, n4
lista = []
lista.append(notas)
print(f'MÉDIA DAS NOTAS = {sum(notas) / len(notas):.2f}')
