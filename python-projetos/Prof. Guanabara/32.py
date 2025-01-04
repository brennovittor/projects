# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.  
from datetime import date

anoatual = date.today().year

while True:
    ano = int(input('Quer analisar um ano?'))

    if ano == 0:
        ano = date.today().year
    if ano > 3000:
        print('Erro, o ano deve ser até 3000 (Coloque 0 para Analisar o Ano atual)')
    elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'o ano {ano} É bissexto')
    else:
        print(f'o ano {ano} Não é  Bissexto')