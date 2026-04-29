while True:

    try:
        name = input('Digite seu nome: ').capitalize()
        height = float(input('Digite sua altura: '))
        weight = int(input('Digite seu peso: '))
        imc = weight / (height * height)
        your_weight = f'Seu IMC é {imc:.2f}'
        print('Calculando...')
    except ValueError:
        print('Valor digitado incorreto.')
        continue
    except ZeroDivisionError:
        print('Peso e altura devem ser maiores que zero.')
        continue

    if imc <= 18.4:
        print(f'{name} você está abaixo do peso')

    elif 18.5 <= imc < 24.9:
        print(f'{name} você está com peso normal')

    elif 25 <= imc < 29.9:
        print(f'{name} você está com pré-obesidade')

    elif 30 <= imc < 34.9:
        print(f'{name} você está com obesidade, grau I')

    elif 35 <= imc < 39.9:
        print(f'{name} você está com obesidade, grau II')

    elif imc > 40:
        print(f'{name} você está com obesidade, grau III')

    else:
        print('Isso não deveria acontecer')

    print(your_weight)
    close = input('Digite (encerrar) ou (e) para encerrar o programa: ').lower()
    if close == 'encerrar' or close == 'e':
        print("Programa encerrado.")
        break

