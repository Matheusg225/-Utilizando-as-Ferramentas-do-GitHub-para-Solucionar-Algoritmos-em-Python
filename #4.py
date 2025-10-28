# 1. Solicita a entrada e converte para inteiro
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")
    exit()

# 2. Utilização de Condicionais (if, else) e Módulo (%)
# O módulo retorna o resto da divisão. Se o resto da divisão por 2 for 0, o número é par.
if numero % 2 == 0:
    resultado = "Par"
else:
    resultado = "Ímpar"

# 3. Exibe o resultado
print(f"\nO número {numero} é {resultado}.")