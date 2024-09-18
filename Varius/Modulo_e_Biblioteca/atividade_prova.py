# importando a bibliteca
import random

def lancar_dados(receive1, receive2):
    # variável que guarda o número sorteado
    receive1 = random.randint(1,6)

    # variável que guarda o número sorteado
    receive2 = random.randint(1,6)

    # somando os números sorteados
    resultado = receive1 + receive2

    return resultado
    
# declarando as váriaveis 
rec1 = ''
rec2 = ''   

# chamando a função
res = lancar_dados(rec1, rec2)
print(f'resultado final {res}')