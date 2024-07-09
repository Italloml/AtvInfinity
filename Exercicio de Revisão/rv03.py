# Notas de alunos utilizando o for
qtd_alunos = int(input("Informe a quantidade de alunos: "))
nome = input("Informe o nome do aluno: ")
soma_notas = 0

for i in range(1, qtd_alunos + 1):
    nota = float(input(f"Informe a nota {i} de {nome}: "))
    soma_notas += nota

media = soma_notas / qtd_alunos

if media >= 7:
    print(f"O aluno {nome} está aprovado com média {media:.2f}")
else:
    print(f"O aluno {nome} está reprovado com média {media:.2f}")

