# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = []

for i in range(7 - 1):
    num = int(input(f'Diga o {i + 1} número:'))
    if num % 2 == 0:
        soma.append(num)

total = sum(soma)
        

print(f'Entre os {i + 1} números, a soma entre os PARES dão: {total}')