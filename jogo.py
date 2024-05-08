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
BRICK_WIDTH=50
BRICK_HEIGHT=25
brick_img=pygame.image.load('Img/01-Breakout-Tiles.png').convert_alpha()
brick_img=pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT))
BAR_WIDHTH=100
BAR_HEIGHT=25
bar_img=pygame.image.load('').convert_alpha()
bar_img=pygame.transform.scale(bar_img, (BAR_WIDHTH, BAR_HEIGHT))
BALL_WIDHTH=100
BALL_HEIGHT=25
ball_img=pygame.image.load('').convert_alpha()
ball_img=pygame.transform.scale(ball_img, (BALL_WIDHTH, BALL_HEIGHT))




#---------- Inicia estrutura de dados
#definindo os novos tipos

class Brick(pygame.sprite.Sprite):
    def __init__(self,img):
        #Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,WIDTH-BRICK_WIDTH)
        self.rect.y = random.randint(0,250)
    # criar(função update(self)) se quiser movimentar o brick


game=True


#Criando Bricks
brick=Brick(brick_img)
#========loop principal========
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        
    # ----- Gera saídas
    window.fill((255,255,255))


    # ----- Desenhando Meteoros

    window.blit(brick.image,brick.rect)

    # ----- Atualiza estado de jogo
    pygame.display.update()

#======Finalização=======
pygame.quit()






