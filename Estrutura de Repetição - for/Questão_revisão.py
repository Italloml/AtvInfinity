# Faça um programa que leia 4 números e informe o maior número, menor e o igual entre eles.

maior = None
menor = None
igual = None

for _ in range(4):
    numero = float(input("Informe: "))
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
    if igual is None or numero == igual:
        igual = numero
    
print(f'maior {maior}')
print(f'menor {menor}')
print(f'igual {igual} || {igual}')