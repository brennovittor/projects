# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nasc = int(input('Em que ano nasceu?: '))
ano_atual = date.today().year
idade = ano_atual - nasc


if idade == 17:
    print('Falta 1 ano para você se alistar')
elif idade < 17:
    saldo = 18 - idade
    print(f'Faltam {saldo} anos para você se alistar')
elif idade > 20:
    saldo = idade - 18
    print(f'Você devia ter se alistado faz {saldo} anos')
elif idade == 18 or 19:
    saldo = idade - 18
    print(f'Você devia ter se alistado faz {saldo} ano')

