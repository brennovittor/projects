tupla = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
    'seis', 'sete', 'oito', 'nove', 'dez', 
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True: 
    try:
        num1 = int(input('Digite um número: '))
        if num1 < 0 or num1 > 20:
            print('Número fora de alcance, por favor digitar novamente')
        else:
            print(tupla[num1])
    except ValueError:
        print('Por favor tente novamente')