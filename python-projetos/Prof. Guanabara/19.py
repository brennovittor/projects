# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

lista = []
for i in range(0, 4):
    alunos = str(input(f'Digite o nome do {i + 1} aluno:'))
    lista.append(alunos)

sortear = random.choice(lista)
print(sortear)