import math as mt

print('_____________________')
print('Vamos calcular o peso real\ndo Leg 45º graus')
print('_____________________')

seno = int(input('Digite o peso:\n'))
calculo = mt.sin(45)*seno

print('O peso real que você está levantando é de {} quilos'.format(calculo))



