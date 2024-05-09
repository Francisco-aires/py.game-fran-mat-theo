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
bar_img = pygame.transform.scale(bar_img, (BAR_WIDHTH, BAR_HEIGHT))


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


class Ball(pygame.sprite.Sprite):
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


class Bar(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
    
    def update(self, keys):
        self.speedx = 0  # Reseta a velocidade cada vez que o update é chamado para evitar movimento contínuo
        if keys[pygame.K_LEFT]:
            self.speedx = -5
        if keys[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        # Mantém a barra dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
game=True

#criando grupo Bricks
all_bricks=pygame.sprite.Group()

#Criando os Bricks
for i in range(25):
    brick=Brick(brick_img)
    all_bricks.add(brick)

#Barrinha criada
bar = Bar(bar_img, WIDTH // 2, HEIGHT - 50) 
#========loop principal========
while game:
    # ----- Trata eventos
    for event in pygame.event.get():

        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # Captura as teclas pressionadas uma vez por frame
    keys = pygame.key.get_pressed()

    # ----- Atualiza estado de jogo
    all_bricks.update()  # os tijolos se movam ou tenham alguma atualização
    bar.update(keys) # Atualiza a posição da barra com base nas entradas do teclado

    # ----- Gera saídas
    window.fill((255,255,255))
    # esta linha é para desenhar a barra
    window.blit(bar.image, bar.rect)
    # Adicione aqui o desenho da bola

    # ----- Desenhando bricks
    all_bricks.draw(window) 
    
    pygame.display.update() # mostra o novo frame para o jogador
#======Finalização=======
pygame.quit()






