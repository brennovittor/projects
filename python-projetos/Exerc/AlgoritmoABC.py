#1 Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.
from time import sleep

A = float(input('Primeiro Valor: '))
B = float(input('Segundo Valor: '))
C = float(input('Terceiro Valor: '))

soma = (A + B)
print(f'A soma entre os valores é igual à: {soma:.0f}')
print('Então é')
print('.')
sleep(1)
print('..')
sleep(1)
print('...')

# Condições aninhadas: IF, ELSE e ELIF

if soma < C:
    print(f'Menor que {C:.0f}')
elif soma == C:
    print(f'Igual a {C:.0f}')
else:
    print(f'Maior que {C:.0f}')