# definindo a função média
def media(numero1, numero2, numero3):
    return (numero1+numero2+numero3)/3
    

# Dados passado pelo usuário
nu1 = int(input("Informe a media 1: "))
nu2 = int(input("Informe a media 2: "))
nu3 = int(input("Informe a media 3: "))

# Chamando a função media
res = media(nu1, nu2, nu3)

# Imprimi na tela
print(f'Numeros informado {nu1}, {nu2}, {nu3} e o resutado {res}')