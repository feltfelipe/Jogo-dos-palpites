'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
'''from random import randint
pc = randint(0, 10)
#player = int(input('Chute um número de 0 a 10: ')) Como colocar esse primeiro input na contagem?
chute = 0
player = ''
while player != pc:
    player = int(input('Chute um número de 0 a 10: '))
    if chute!= pc:
        chute+= 1
print('ACERTOU MISERÁVI !!')
print('O computador escolheu o número {}'.format(pc))
print('Você precisou de {} tentativas para acertar.'.format(chute))'''

from random import randint
from time import sleep


computador = randint(0, 10)
palpites = 0
print('Sou seu computador...Vou pensar num número de 0 a 10.')
sleep(3)
print('...pensando...')
sleep(2)
print('Pronto!! Será que você consegue advinhar qual foi?')

while True: #enquanto acertou não for verdadeiro (True):
    jogador = int(input('Qual seu palpite? ')) #peça um input do usuário e salve como jogador
    palpites += 1 #adicione 1 para contagem de palpites toda vez que jogar fizer um input.
    if jogador == computador: #se jogador acertar o número do computador, então:
        #acertou = True #acertou passa a ser verdadeiro.
        break;
    else: #se jogador não for igual computador , então:
        if jogador < computador: #se jogador for menor que computador:
            print('Mais...tente mais uma vez') #diga que precisa chutar mais alto
        elif jogador > computador: #senão:
            print('Menos...tente mais uma vez') #peça para chutar mais baixo
print(f'Acertou!! Você precisou de {palpites} tentativas para acertar.') #se acertou for verdadeiro, encerre e diga quantos palpites precisou para acertar!
