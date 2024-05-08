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
BRICK_WIDTH=150
BRICK_HEIGHT=100
brick_img=pygame.image.load('Img/01-Breakout-Tiles.png').convert_alpha()
brick_img=pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT))



#---------- Inicia estrutura de dados
#definindo os novos tipos

class Brick(pygame.sprite.Sprite):
    def __init__(self,img):
        #Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-BRICK_WIDTH)
        self.rect.y = random.randint(-250, 0)
    # criar(função update(self)) se quiser movimentar o brick
class Ball(pygaem.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 950
        self.speedx = 0
        self.speedy = 5
    def update (self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect = WIDTH
            self.speedx = -self.speedx
        if self.rect.left < 0:
            self.rect = 0
            self.speedx = -self.speedx 


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






