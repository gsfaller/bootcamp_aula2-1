# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

num_1 = int(input("Insira 1 número:"))
num_2 = int(input("Insira 2 número:"))
print(num_1 + num_2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

num_resto = int(input("Insira um número para ser dividido por 5 e retornar apenas o resto da divisão:"))
resto_divisao = (num_resto % 5)
print(f"O resto da sua divisão é: {resto_divisao}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

print("Neste exercício você irá multiplicar dois números.")
num_3 = int(input("Insira o primeiro número:"))
num_4 = int(input("Insira o segundo número:"))

multiplicacao = num_3 * num_4
print(f"A multiplicação dos dois números inseridos é: {multiplicacao}")


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

print("Neste exercício você irá realizar uma divisão inteira do primeiro número pelo segundo.")
try: 
    num_5 = int(input("Insira o primeiro número, por favor:"))
    num_6 = int(input("Insira o segundo número, por favor:"))
    resultado = num_5 // num_6
    print(resultado)
except ZeroDivisionError:
    print("integer division or modulo by zero")
except KeyboardInterrupt:
    print("acho que você interrompeu o programa")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

print("Neste exercício você irá multiplicar dois números.")
num_7 = int(input("Insira o primeiro número:"))
num_8 = int(input("Insira o segundo número:"))
multiplicacao = num_7 * num_8
if multiplicacao != 0:
    print(f"A multiplicação dos dois números inseridos é: {multiplicacao}")
else:
    print("Por favor, rode de novo o programa e insira um número diferente de zero.")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
    
num_9 = float(input("Insira um número com vírgula para realizarmos uma adição de números não inteiros."))
num_10 = float(input("Insira outro número com vírgula para realizarmos uma adição de números não inteiros."))
if isinstance(num_9, float):
    if isinstance(num_10, float):
        soma_float = num_9 + num_10
        print(f"A soma dos números não inteiros é = {soma_float}")
    else:
        print("Insira um número no formato solicitado")
else:
    print("Insira um número no formato solicitado")

    
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
    
media_float = (soma_float / 2)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

numero_base = input("Insira o número que será elevado a potência fornecida em sequência:")
exponencial = input("Insira a exponencial do número anterior:")

resultado_exponencial = numero_base ** exponencial

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

temp_celsius = int(input("Insira a temperatura em Celsius:"))
fahrenheit = (temp_celsius * 9/5 ) + 32

print(fahrenheit)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = int(input("Insira o valor do raio"))
area = 3.14 * (raio ** 2)

print(area)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.



# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if
    
    # ex

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
