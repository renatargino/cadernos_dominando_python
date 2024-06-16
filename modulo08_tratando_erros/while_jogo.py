# jogo da adivinhação
from random import randint

print('*****************************************')
print('Seja bem vind0(a) ao jogo de adivinhação!')
print('*****************************************')

print('\n')

numero_secreto = randint(1,5)
numero_escolhido = 0

while numero_secreto != int(numero_escolhido):
    numero_escolhido = input('Escolha um número de 1 a 5: ')
    if numero_escolhido not in range(1,5):
        raise Exception('Este jogo não aceita outros números e/ou letras! Tente novamente!')


print(f'Parabéns! Você descobriu que o número secreto era o {numero_secreto}!')