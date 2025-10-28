# Solicita a palavra e a normaliza (remove espaços e torna minúscula)
palavra_original = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
palavra_limpa = palavra_original.lower().replace(" ", "")

# Inversão da String usando slicing
palavra_invertida = palavra_limpa[::-1]

# Verifica se é um palíndromo
resultado = "é um palíndromo" if palavra_limpa == palavra_invertida else "NÃO é um palíndromo"

# Exibe o resultado
print(f"\nA palavra ou frase '{palavra_original}' {resultado}.")
