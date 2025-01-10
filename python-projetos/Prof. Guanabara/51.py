# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Termo: '))
razao = int(input('Razão: '))

for c in range(termo, termo + 10 * razao, razao):
    print(c, end=' > ')
print('Acabou')