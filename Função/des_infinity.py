# declaração da função
def maior_numero(nu1, nu2, nu3):
    if nu1 > nu2 and nu1 > nu3:
        return nu1
    elif nu2 > nu1 and nu2 > nu3:
        return nu2
    else:
        return nu3

# interação com o usuário 
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

# chamar a função
receive = maior_numero(n1, n2, n3)

# printar na tela
print(f'Os números {n1}, {n2}, {n3} entre eles, o maior é: {receive}')