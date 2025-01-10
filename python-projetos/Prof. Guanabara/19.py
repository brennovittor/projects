# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

# Lista para armazenar os nomes dos alunos
lista = []

# Coletando os nomes dos alunos
for i in range(0, 4):
    alunos = str(input(f'Digite o nome do {i + 1}º aluno: '))
    lista.append(alunos)

# Sorteando um aluno aleatoriamente
sortear = random.choice(lista)

# Exibindo o nome do aluno sorteado
print(f'O aluno sorteado para apagar o quadro é: {sortear}')
