preco = float(input('Qual o preço do produto? '))
porcento = (preco / 100) * 5
novopreco = preco - porcento
print('O preco do produto com desconto de 5% é R$ {:.2f}'.format(novopreco))