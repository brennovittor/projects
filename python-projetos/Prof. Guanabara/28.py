import random

while True:
    n1 = random.randint(0, 5)
    n2 = int(input('Em qual número eu pensei? (de 1 a 5)'))

    if n2 == n1:
        print('Está correto')
        break
    else:
        print('Tente novamente')