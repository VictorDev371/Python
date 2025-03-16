print('DESAFIO 013')

s= float(input('Qual o valor do salario? '))
p= int(input('Qual é a porcentagem de aumento? '))
au= (s*p)/100
ns= s+au
print('')

print('O novo salário do escravo vai ser {:.2f} com o aumento de 15%'.format(ns))
print('')