dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
totdias = dias * 60
totkm = km * 0.15
total = totkm + totdias
print('O total a pagar é de R$ {:.2f}'.format(total))