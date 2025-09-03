while True:

    name = input('Digite seu nome: ')
    height = float(input('Digite sua altura: '))
    weight = int(input('Digite seu peso: '))
    imc = weight / (height * height)

    if imc <= 18.5:
        print(f'{name} você está abaixo do peso')
        print(f'Seu peso é {imc:.2f}')

    elif 18.6 <= imc < 24.9:
        print(f'{name} você está com peso normal')
        print(f'Seu peso é {imc:.2f}')

    elif 25 <= imc < 29.9:
        print(f'{name} você está com pré-obesidade')
        print(f'Seu peso é {imc:.2f}')

    elif 30 <= imc < 34.9:
        print(f'{name} você está com obesidade, grau I')
        print(f'Seu peso é {imc:.2f}')

    elif 35 <= imc < 39.9:
        print(f'{name} você está com obesidade, grau II')
        print(f'Seu peso é {imc:.2f}')

    elif imc > 40:
        print(f'{name} você está com obesidade, grau III')
        print(f'Seu peso é {imc:.2f}')

    else:
        print("Peso e altura devem ser maiores que zero.")

    close = input('Digite (encerrar) ou (e) para encerrar o programa: ').lower()
    if close == 'encerrar' or close == 'e':
        print("Programa encerrado.")
        break

