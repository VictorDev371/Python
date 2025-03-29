
velocidade= float(input('Qual a velocidade do carro (apenas o valor)? '))
multa= (velocidade-80)*7
print('')

if velocidade > 80:
    print('Você ultrapassou a velocidade límite de 80km/h, por isso vai pagar uma multa de {}'.format(multa))
else:
    print('Muito bem, sigua em frente na sua rota.')