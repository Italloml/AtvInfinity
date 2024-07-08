# Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser. 
# Exercício de revisão Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

soma = 0
accept = True
contador = 0
check = input("Deseja continuar? s - sim // n - não")
while accept: 
    if check == 's' or contador > 5:
        numero = int(input("Informe: ")) 
        soma += numero
        contador += 1
    else:
        accept = False

print(f"resultado da soma de numeros: {soma}")

# em desenvolvimento...