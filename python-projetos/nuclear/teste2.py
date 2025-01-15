# Modúlo num2words (Escrever números por extenso, aula Prof. Guanabara #72, Aprimorando)

from num2words import num2words

print('Welcome, este é um conversor de números')
print('=-' * 30)
while True:
    try:
        numero = int(input('Digite um número: '))
        print(num2words(numero, lang='pt_BR'))
    except ValueError:
        print('Erro, tente novamente')
