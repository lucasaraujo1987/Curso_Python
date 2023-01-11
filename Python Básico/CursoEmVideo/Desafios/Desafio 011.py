altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
litro = area / 2
print('Com a parede de {:.2f} metros de altura e {:.2f} metros de largura, você tem {:.3f} m² e precisará de {:.4f} litros de tinta'.format(altura, largura, area, litro))