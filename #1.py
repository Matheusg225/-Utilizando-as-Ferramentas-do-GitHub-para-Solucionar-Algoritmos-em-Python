# 1. Solicita a primeira entrada de dados
# 1. Solicita uma string
texto = input("Por favor, digite um texto: ")

# 2. Solicita um número inteiro
numero = int(input("Agora, digite um número inteiro: "))

# 3. Repete a string o número de vezes especificado
resultado = texto * numero

# 4. Exibe o resultado
print("\n--- Resultado da Repetição ---")
print(f"Texto digitado: {texto}")
print(f"Número de repetições: {numero}")
print(f"Resultado final: {resultado}")
