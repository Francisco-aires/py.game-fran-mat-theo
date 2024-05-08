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
BALL_WIDHTH=20
BALL_HEIGHT=20
ball_img=pygame.image.load('').convert_alpha()
ball_img=pygame.transform.scale(ball_img, (BALL_WIDHTH, BALL_HEIGHT))




#---------- Inicia estrutura de dados
#lista posições bricks
lista_x=[]
lista_y=[]
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
    def update(self):
        self.rect.x=self.rect.x  #  ((compoletar função update))


game=True

#criando grupo Bricks
all_bricks=pygame.sprite.Group()

#Criando os Bricks
for i in range(25):
    brick=Brick(brick_img)
    all_bricks.add(brick)
#========loop principal========
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False


    # ----- Atualiza estado de jogo

    # ----- Gera saídas
    window.fill((255,255,255))

     # ----- Desenhando bricks
    all_bricks.draw(window) 
    
    pygame.display.update() # mostra o novo frame para o jogador
#======Finalização=======
pygame.quit()






