import random
import string

def gerador_senha():
    while True:pip install -r requirements.txt

        # Solicita ao usuário o tamanho da senha
        try:
            tamanho = int(input("Digite o tamanho desejado para a senha: "))
            if tamanho > 100:
                print("A senha deve ter no máximo 100 caracteres!")
                continue
        except ValueError:
            print("Por favor, digite um número válido!")
            continue

        # Solicita ao usuário as opções
        incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower()
        incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower()
        incluir_numeros = input("Incluir números? (s/n): ").lower()
        incluir_caracteres = input("Incluir caracteres especiais? (s/n): ").lower()

        # Cria o conjunto de caracteres permitidos
        caracteres = ''
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_caracteres:
            caracteres += string.punctuation

        # Verifica se o conjunto de caracteres é vazio
        if not caracteres:
            print("Você deve incluir pelo menos um tipo de caractere.")
            continue

        # Gera a senha aleatória
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        print(f"Sua senha gerada é: {senha}")

        # Oferece ao usuário a opção de gerar outra senha
        repetir = input("Deseja gerar outra senha? (s/n): ").lower()
        if repetir != 's':
            print("Programa encerrado!")
            break

# Chama a função
gerador_senha()
