#====== Inicialização=======

#---------- Importa e inicia pacotes
import pygame
import random

pygame.init()

#---------- Gera tela principal
WIDTH=400
HEIGHT=500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('BREAKOUT INSPER')




#---------- Inicia estrutura de dados
#definindo os novos tipos

class Brick(pygame.sprite.Sprite):
    def __init__(self,img)

game=True
#========loop principal========
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        
    # ----- Gera saídas


    # ----- Atualiza estado de jogo
    pygame.display.update()

#======Finalização=======
pygame.quit()






