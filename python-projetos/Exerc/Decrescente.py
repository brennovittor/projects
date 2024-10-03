#Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

valores = []

for i in range(3):
    i = int(input(f"{i + 1}º Valor: "))
    valores.append(i)

valores.sort(reverse=True)

print(valores)