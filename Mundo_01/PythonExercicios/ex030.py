# Exercício Python 030: Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('\033[35mMe diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('\033[37mO número {} é \033[34mPAR'.format(numero))
else:
    print('\033[37mO número {} é \033[34mÍMPAR'.format(numero))
