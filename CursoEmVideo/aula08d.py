#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
m = float(input('Digite um numero real: '))
print('{}'.format(trunc(m)))
