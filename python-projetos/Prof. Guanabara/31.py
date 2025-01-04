# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input('Qual a distância percorrida em KM? : '))

if km < 200:
    taxa = km * 0.50
    print(f'o valor total da corrida foi de aproximadamente R${taxa:.2f}')
else:
    taxa = km * 0.45
    print(f'o valor total da corrida foi de aproximadamente R${taxa:.2f}')
