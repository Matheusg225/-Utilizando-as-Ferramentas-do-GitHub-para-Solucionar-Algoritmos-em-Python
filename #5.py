# 5 - Calculando Média de Notas 📚 - Versão Corrigida

# 5 - Calculando Média de Notas 📚 - Versão Corrigida

# Função auxiliar para garantir que a entrada seja um número (mesmo com vírgula)
def obter_nota(prompt):
    while True:
        entrada = input(prompt)
        # Troca a vírgula (,) por ponto (.) para o Python entender como float
        entrada_tratada = entrada.replace(",", ".")
        try:
            return float(entrada_tratada)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número (use ponto ou vírgula).")

# 1. Solicita as três notas usando a função de tratamento
print("Vamos calcular a média de 3 notas.")

nota1 = obter_nota("Digite a primeira nota: ")
nota2 = obter_nota("Digite a segunda nota: ")
nota3 = obter_nota("Digite a terceira nota: ")

# 2. Cálculo da Média
soma_das_notas = nota1 + nota2 + nota3
media = soma_das_notas / 3

# 3. Exibe o resultado
print("\n--- Resultado da Média ---")
print(f"A soma das notas é: {soma_das_notas:.2f}")
print(f"A média das notas é: {media:.2f}")