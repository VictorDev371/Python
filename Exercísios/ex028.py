import random
numero= int(input('Qual o número que você chuta? '))
lista= [0, 1, 2, 3, 4, 5]
if numero== random.choice(lista):
    print('PARABÉNS, VOCÊ ACERTOU O NÚMERO!!!')
else:
    print('Nah, I win')
