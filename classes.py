#imports
import time
import pygame
import random

from jogo import *
###########
# classes #
###########

# brick
class Brick(pygame.sprite.Sprite):
    def __init__(self,img):
        #Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        condicao=True
        while condicao:
            lista_par=[] #lista com as coordenadas do brick para verificar se essa esta livre
            x= random.choice(lista_x)
            y=random.choice(lista_y)
            lista_par.append(x)
            lista_par.append(y)
            if lista_par in lista_bricks:   #Modificar caso já esteja lotado
                condicao=True
            else:
                condicao=False
                lista_bricks.append(lista_par)
  
        self.rect.x = x
        self.rect.y = y
    # criar(função update(self)) se quiser movimentar o brick
    def update(self):
        self.rect.x=self.rect.x  #  ((compoletar função update))