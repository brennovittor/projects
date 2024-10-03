# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

var = input('Diga qualquer coisa: ')
print('Este tipo primitivo de valor é', type(var))
print('Ele tem somente espaços?: ', var.isspace())
print('É um número?: ', var.isnumeric())

