#====== Inicialização=======

#---------- Importa e inicia pacotes
import pygame
import random

pygame.init()

#---------- Gera tela principal
WIDTH=1000
HEIGHT=500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('BREAKOUT INSPER')


# ------ Incia Assets
BRICK_WIDTH=20
BRICK__HEIGHT=10
brick_img=pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha()
brick_img=pygame.transform.scale(brick_img, (METEOR_WIDTH, METEOR_HEIGHT))



#---------- Inicia estrutura de dados
#definindo os novos tipos

class Brick(pygame.sprite.Sprite):
    def __init__(self,img):
        #Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
        self.rect.y = random.randint(-100, -METEOR_HEIGHT)

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






