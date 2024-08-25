pesos = float(input('Sobra em pesos:'))
reais = float(input('Sobra em reais:'))

conpenusd = pesos / 0.001073
conreausd = reais / 0.1747

print('O total em dólar dos seus pesos é de: {:.2f} USD' .format(conpenusd))
print('O total em dólar dos seus reais é de: {:.2f} USD' .format(conreausd))

SobraTotal = conpenusd + conreausd
print('O total em dólar de todas as sobras é de {:.2f} USD' .format(SobraTotal))
