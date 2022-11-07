from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-' * 10)
print('O computador escolheu {}' .format(itens[computador]))
print('Jogador jogou {}' . format(itens[jogador]))
print('-' * 10)
if computador == 0: #computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
         print('VOCÊ PERDEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou Papel
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
         print('VOCÊ GANHOU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #computador jogou Tesoura
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
         print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
