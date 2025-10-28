# 1. Solicita a primeira entrada numérica
# O input será convertido para 'float' para aceitar números decimais, não apenas inteiros.
try:
    num1 = float(input("Digite o primeiro número: "))
except ValueError:
    print("Erro: Entrada inválida para o primeiro número.")
    exit()

# 2. Solicita a segunda entrada numérica
# 1. Solicita a primeira entrada numérica
try:
    num1 = float(input("Digite o primeiro número: "))
except ValueError:
    print("Erro: Entrada inválida para o primeiro número.")
    exit()

# 2. Solicita a segunda entrada numérica
try:
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("Erro: Entrada inválida para o segundo número.")
    exit()

# 3. Realiza e armazena as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verifica se o segundo número é zero antes de dividir
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero"

# 4. Exibe os resultados
print("\n--- Resultados das Operações ---")
print(f"Soma ({num1} + {num2}): {soma}")
print(f"Subtração ({num1} - {num2}): {subtracao}")
print(f"Multiplicação ({num1} * {num2}): {multiplicacao}")
print(f"Divisão ({num1} / {num2}): {divisao}")

# 3. Realiza e armazena as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verifica se o segundo número é zero antes de dividir
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero"

# 4. Exibe os resultados
print("\n--- Resultados das Operações ---")
print(f"Soma ({num1} + {num2}): {soma}")
print(f"Subtração ({num1} - {num2}): {subtracao}")
print(f"Multiplicação ({num1} * {num2}): {multiplicacao}")
print(f"Divisão ({num1} / {num2}): {divisao}")