#exercicio 1
def calcular_salario(salario_por_hora, horas_trabalhadas):
    salario_total = salario_por_hora * horas_trabalhadas
    return salario_total

# Exemplo de uso da função
def main():
    salario_por_hora = float(input("Digite o salário por hora: "))
    horas_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))

    salario_final = calcular_salario(salario_por_hora, horas_trabalhadas)
    print(f"O salário a ser recebido é: R${salario_final:.2f}")

if __name__ == "__main__":
    main()

#exercicio 2
def calcular_exibicao_numeros(num1, num2, num3):
    resultado1 = (2 * num1) * (0.5 * num2)
    resultado2 = (3 * num1) + num3
    resultado3 = num3 ** 3

    print(f"Resultado 1: O produto do dobro do primeiro com metade do segundo é {resultado1}")
    print(f"Resultado 2: A soma do triplo do primeiro com o terceiro é {resultado2}")
    print(f"Resultado 3: O terceiro elevado ao cubo é {resultado3}")

# Exemplo de uso da função
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

calcular_exibicao_numeros(num1, num2, num3)

#exxercicio 3
def calcular_resultados(num1, num2, num3):
    resultado1 = (2 * num1) * (0.5 * num2)
    resultado2 = (3 * num1) + num3
    resultado3 = num3 ** 3

    return resultado1, resultado2, resultado3

# Exemplo de uso da função
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado1, resultado2, resultado3 = calcular_resultados(num1, num2, num3)

print(f"Resultado 1: O produto do dobro do primeiro com metade do segundo é {resultado1}")
print(f"Resultado 2: A soma do triplo do primeiro com o terceiro é {resultado2}")
print(f"Resultado 3: O terceiro elevado ao cubo é {resultado3}")

#exercicio 4
def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Exemplo de uso da função
ano = int(input("Digite um ano: "))
if eh_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
