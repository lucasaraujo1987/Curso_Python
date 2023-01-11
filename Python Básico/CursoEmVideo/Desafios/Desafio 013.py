salario = float(input('Qual o seu salário? '))
porcento = (salario / 100) * 15
novosalario = salario + porcento
print('O salário com 15% de aumento é R$ {:.2f}'.format(novosalario))