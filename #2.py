# Solicita uma string e um número inteiro (não-negativo) e repete a string esse número de vezes.

texto_original = input("Digite o texto que você quer repetir: ")

while True:
    entrada_repeticoes = input("Digite quantas vezes o texto deve ser repetido (número inteiro não-negativo): ")
    try:
        numero_repeticoes = int(entrada_repeticoes)
        if numero_repeticoes < 0:
            print("Por favor, digite um número inteiro NÃO-NEGATIVO.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite APENAS um número inteiro.")

resultado_repetido = texto_original * numero_repeticoes

print("\n--- Resultado da Repetição de Textos ---")
print(f"Texto fornecido: '{texto_original}'")
print(f"Repetido {numero_repeticoes} vezes.")
print(f"Resultado final:\n{resultado_repetido}")
