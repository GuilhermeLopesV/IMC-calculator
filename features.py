def bmi_calculator(imc, name):
    if imc <= 18.4:
        print(f'{name} você está abaixo do peso')
        return

    elif 18.5 <= imc < 24.9:
        print(f'{name} você está com peso normal')
        return

    elif 25 <= imc < 29.9:
        print(f'{name} você está com pré-obesidade')
        return

    elif 30 <= imc < 34.9:
        print(f'{name} você está com obesidade, grau I')
        return

    elif 35 <= imc < 39.9:
        print(f'{name} você está com obesidade, grau II')
        return

    elif imc > 40:
        print(f'{name} você está com obesidade, grau III')
        return

    else:
        print('Isso não deveria acontecer')