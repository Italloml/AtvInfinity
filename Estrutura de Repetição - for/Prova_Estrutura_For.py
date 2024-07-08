# Solicita o inicio e o fim
inicio = int(input("Informe o inicio do intervalo: "))
fim = int(input("Informe o final do intervalo: "))
soma = 0
# loop que vai do inicio ao fim do laço
for i in range(inicio, fim + 1):
    if i % 2 == 0: # Verifica o número par
        soma += i
else:
    if soma == 0:
            print(f'Nesse intervalo {inicio} e {fim} não tem pares')
    else:
        print(f'Soma de números pares: {soma}')
