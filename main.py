from features import bmi_calculator

while True:

    try:
        name = input('Digite seu nome: ').capitalize()
        height = float(input('Digite sua altura: '))
        weight = int(input('Digite seu peso: '))
        imc = weight / (height * height)
        your_IMC = f'Seu IMC é {imc:.2f}'
        print('Calculando...')
    except ValueError:
        print('Valor digitado incorreto.')
        continue
    except ZeroDivisionError:
        print('Peso e altura devem ser maiores que zero.')
        continue

    bmi_calculator(imc, name)

    print(your_IMC)
    close = input('Digite (encerrar) ou (e) para encerrar o programa: ').lower()
    if close == 'encerrar' or close == 'e':
        print("Programa encerrado.")
        break

