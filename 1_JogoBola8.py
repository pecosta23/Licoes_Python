import random as rd

print('Jogo da bola oito, perguntas com sim ou não\n')

pergunta = input('Digite sua pergunta:')

pergunta = rd.randint(1,6)
if pergunta == 1:
        print('Muito provável')
elif pergunta == 2:
    print('Pouco provável')
elif pergunta == 3:
    print('Sem chance de acontecer')
elif pergunta == 4:
    print('teu pai')
elif pergunta == 5:
    print('Melhor eu não te falar isso agora...')
elif pergunta == 6:
    print('Pode acontecer')

