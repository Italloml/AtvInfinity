# pedir para o usuário um número
numero = int(input("Informe um numero: "))

# verificação
if (numero > 0):
    print(f'{numero} é positivo!')
elif(numero < 0):
    print(f'{numero} é negativo!')
else:
    print(f'É zero')