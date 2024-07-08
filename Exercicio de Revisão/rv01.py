horasTrabalhada = float(input("Informe quanto ganha por horas: "))
horasMes = float(input("Informe quantas horas trabalhou no mês: "))

# salário bruto
salBruto = horasTrabalhada * horasMes

# desconto de IR
descIr = salBruto - (salBruto * (11/100))

# desconto de INSS
descInss = salBruto - (salBruto * (8/100))

# desconto para sindicato
descSind = salBruto - (salBruto * (5/100))

# salario liquido
salLiquido = descIr - descInss - descSind

print(f'Salário bruto: {salBruto}')
print(f'Quanto pagou ao INSS: {descInss}')
print(f'Quanto pagou ao sindicato: {descSind}')
print(f'Salário liquido: {salLiquido}')