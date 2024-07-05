# Importação da biblioteca
import random
# Gerar um número aleatório entre 1 e 10
numeroSecreto = random.randint(1, 10)
# Número máximo de tentativas
tentMaximas = 3
tentativas = 0
while tentativas < tentMaximas:
    # Pedir ao jogador para adivinhar o número
    try:
        tentativa = int(input("Adivinhe o número (entre 1 e 10): "))
    except ValueError:
        print("Número incorreto, informe um válido.")
        continue
    # ver se a tentativa é a correta
    if tentativa == numeroSecreto:
        print("Você acertou, parabéns.")
        break
    else:
        print("Está incorreto.")
        tentativas += 1
        if tentativas < tentMaximas:
            print("Errou, tenta de novo.")
        else:
            print(f"Tentativa acabada. O número correto é: {numeroSecreto}.")

