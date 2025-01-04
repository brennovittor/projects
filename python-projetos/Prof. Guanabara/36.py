# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa em R$: '))
salario = float(input('Diga seu sálario em R$: '))
anos = float(input('Em quantos anos você pretende pagar esse valor?: '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100


if minimo < prestacao:
    print('Desculpe, não podemos negociar esta oferta')
else:
    print(f'Para pagar uma casa de R${casa:.0f} com {anos:.0f} anos, a prestação seria de {prestacao:.0f} reais')
