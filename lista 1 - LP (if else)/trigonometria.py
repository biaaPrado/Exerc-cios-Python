import math

angulo = int(input('Digite um angulo em graus: '))
rad = math.radians(angulo)

if (90 > angulo >= 0 or
        270 >= angulo > 180):
    print('O cosseno de', angulo, 'é', math.cos(rad), 'e pertence ao quadrante ímpar')

elif (180 >= angulo > 90 or
      360 >= angulo > 270 ):
    print('O seno de', angulo, 'é', math.sin(rad), 'e pertence ao quadrante par')