larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
tinta = area/2
print('Sua parede tem a diemnsão de {}x{} e sua area é de {}metros quadrados'.format(larg,alt,area))
print('Para pintar essa parede, você precisara de {} litros de tinta'.format(tinta))