# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num1 = int(input('Digite um número: '))

if num1 < 2:
    print('N é primo')
else:
    is_primo = True

for c in range(2, num1):
    if num1 % c == 0:
        is_primo = False

if is_primo:
    print('é primo')
else:
    print('N é primo')