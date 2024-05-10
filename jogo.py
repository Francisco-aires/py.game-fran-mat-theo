#====== Inicialização=======

#---------- Importa e inicia pacotes
import pygame
import random

pygame.init()

#---------- Gera tela principal
WIDTH=850
HEIGHT=600
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('BREAKOUT INSPER')


# ------ Incia Assets
BRICK_WIDTH=50
BRICK_HEIGHT=25
brick_img=pygame.image.load('Img/01-Breakout-Tiles.png').convert_alpha()
brick_img=pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT))

BAR_WIDHTH=100
BAR_HEIGHT=25
bar_img=pygame.image.load('Img/17-Breakout-Tiles.png').convert_alpha()
bar_img = pygame.transform.scale(bar_img, (BAR_WIDHTH, BAR_HEIGHT))


BALL_WIDHTH=20
BALL_HEIGHT=20
ball_img=pygame.image.load('Img/58-Breakout-Tiles.png').convert_alpha()
ball_img=pygame.transform.scale(ball_img, (BALL_WIDHTH, BALL_HEIGHT))

# telinhaaaa de inicio funçao
def tela_inicio(window):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                running = False

        window.fill((0, 0, 0))  # Define a cor de fundo da tela de início
        font = pygame.font.Font(None, 36)  # Define a fonte

        # Cria um texto de boas-vindas
        texto_inicio = font.render('Bem-vindo ao BREAKOUT INSPER!', True, ((255, 255, 255)))
        inicio_rect = texto_inicio.get_rect(center=(WIDTH / 2, HEIGHT / 3))

        # Cria um texto de instrução
        instrucao = font.render('Pressione qualquer tecla para começar', True, ((255, 255, 255)))
        instrucao_rect = instrucao.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        # Desenha os textos na tela
        window.blit(texto_inicio, inicio_rect)
        window.blit(instrucao, instrucao_rect)

        pygame.display.update()  # Atualiza a tela para mostrar os textos

def tela_fim(window):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                running = False

        window.fill((0, 0, 0))  # Define a cor de fundo da tela de Game Over
        font = pygame.font.Font(None, 36)  # Define a fonte

        # Cria um texto de Game Over
        texto_fim = font.render('GAME OVER', True, ((255, 0, 0)))
        fim_rect = texto_fim.get_rect(center=(WIDTH / 2, HEIGHT / 3))

        # Cria um texto de instrução
        instrucao = font.render('Pressione qualquer tecla para recomeçar', True, ((255, 255, 255)))
        instrucao_rect = instrucao.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        # Desenha os textos na tela
        window.blit(texto_fim, fim_rect)
        window.blit(instrucao, instrucao_rect)

        pygame.display.update()

############### carregar sons #####################
# Carrega o som de colisão
som_colisao = pygame.mixer.Sound('sons/somco.mp3')
#        som_colisao.play() se quiser tocar

# Carrega a música de fundo
pygame.mixer.music.load('sons/name.mp3')


#---------- Inicia estrutura de dados
#lista posições bricks
lista_x=[10,70,130,190,250,310,370,430,490,550,610,670,730,790,]
lista_y=[5,35,65,95,125,155,185,215,245]
lista_bricks=[]#lista com a posição de todos os blocos
#definindo os novos tipos

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


class Ball(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img  # Define a imagem da bola
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 250
        self.mask = pygame.mask.from_surface(self.image)
        self.real_x = float(self.rect.x)  # Posição X real como ponto flutuante
        self.real_y = float(self.rect.y)  # Posição Y real como ponto flutuante
        self.speedx = 0 # velocidade inicial
        self.speedy = 5  # Velocidade negativa para mover a bola para cima inicialmente
        self.condicao_hit_ball_bar=0

    def update (self):
        # Atualiza as posições reais com as velocidades
        self.real_x += self.speedx
        self.real_y += self.speedy
        # Atualiza as posições do retângulo com valores inteiros
        self.rect.x = int(self.real_x)
        self.rect.y = int(self.real_y)        
        # Rebate nos ladosss
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speedx = -self.speedx
        # Rebate a bola na borda superior
        if self.rect.top < 0:
            self.speedy = -self.speedy
        # nao sei o que fazer no chao
        if self.rect.bottom > HEIGHT: # teleportando pro inicio
            self.rect.x = 500
            self.rect.y = 250
            self.real_x = float(self.rect.x)  # Posição X real como ponto flutuante
            self.real_y = float(self.rect.y)  # Posição Y real como ponto flutuante
        


class Bar(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.real_x = x  # pra barrinha ir mais devagar
    
    def update(self, keys):
        self.speedx = 0  # Reseta a velocidade cada vez que o update é chamado para evitar movimento contínuo
        if keys[pygame.K_LEFT]:
            self.speedx = -5
        if keys[pygame.K_RIGHT]:
            self.speedx = 5
        self.real_x += self.speedx
        self.rect.x = int(self.real_x) #tranformar em numero inteiro

        # Mantém a barra dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.real_x = self.rect.x # sintonizar com a posicao real
        if self.rect.left < 0:
            self.rect.left = 0
            self.real_x = self.rect.x # sintonizar com a posicao real


class Powers(pygame.sprite.Sprite):
    def __init__(self, power_img, center, bottom):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(power_img) # Escolhe qual dos poderes será usado
        self.rect = self.image.get_rect()
        self.rect.centerx = center
        self.rect.bottom = bottom
        self.speedy = 5
    def update(self):
        self.rect.y += self.speedy # Atualiza o poder com sua velocidade padrão
        if self.rect.bottom < 0:
            self.kill() # Apaga o sprite do poder caso ele saia da tela
    def power_up(self, power_numbers):
        power = power_numbers[self.image] # Acha qual é o poder dependendo de qual imagem foi escolhida
        a=0
        if power == 1:
            a=1
        if power == 2:
            a=2
        if power == 3:
            a=3





game=True

#criando grupo Bricks
all_sprites = pygame.sprite.Group()
all_bricks=pygame.sprite.Group()
all_balls=pygame.sprite.Group()

#Criando os Bricks
for i in range(100):
    brick=Brick(brick_img)
    all_bricks.add(brick)
    all_sprites.add(brick)

#Barrinha criada
bar = Bar(bar_img, WIDTH // 2, HEIGHT - 50) 
all_sprites.add(bar)

condicao_hit_ball_bar=0

#bolinhaaaaaaaaaaaaaa
ball = Ball(ball_img)
all_sprites.add(ball)
all_balls.add(ball)


tela_inicio(window)

# Inicia a reprodução da música de fundo em loop
pygame.mixer.music.play(-1)

# Variável que ajusta velocidde[
clock = pygame.time.Clock()
FPS = 60

#========loop principal========
while game:

    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():

        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # Captura as teclas pressionadas uma vez por frame
    keys = pygame.key.get_pressed()

    # ----- Atualiza estado de jogo

    #atualiza posições (barra e bola)
    all_bricks.update()  # os tijolos se movam ou tenham alguma atualização
    bar.update(keys) # Atualiza a posição da barra com base nas entradas do teclado
    ball.update() #bolinha movendoo

    #verifica se houve colisão
    # colizao da bolinha X bloco
    hits_ball_brick=pygame.sprite.groupcollide(all_balls, all_bricks, False, True, pygame.sprite.collide_mask)
    # colizao com o bloco inverte a bola
    for ball, bricks_hit in hits_ball_brick.items():
        if len(bricks_hit)==1:
            brick = bricks_hit[0]  # Pega o primeiro tijolo atingido
        
        if len(bricks_hit)==2:
            brick=bricks_hit[0]
            ball_center = ball.rect.centerx
            brick_center = brick.rect.centerx

            #verifia se a colisão foi diferente
            if abs(ball_center - brick_center) < brick.rect.width / 2:
                # A colisão é mais provavelmente superior ou inferior
                ball.speedy = -ball.speedy
            else:
                # A colisão é mais provavelmente lateral
                ball.speedx = -ball.speedx
            brick=bricks_hit[1]

        # Verifica se a colisão foi mais lateral do que superior/inferior
        # Comparando o centro da bola com o centro do tijolo
        ball_center = ball.rect.centerx
        brick_center = brick.rect.centerx

        # Verifica se a colisão foi mais lateral
        if abs(ball_center - brick_center) < brick.rect.width / 2:
            # A colisão é mais provavelmente superior ou inferior
            ball.speedy = -ball.speedy
        else:
            # A colisão é mais provavelmente lateral
            ball.speedx = -ball.speedx

    # colizao da barrinha X bolinha
    hits_ball_bar=pygame.sprite.spritecollide(bar,all_balls,False,pygame.sprite.collide_mask)
    if len(hits_ball_bar)> ball.condicao_hit_ball_bar:
        ball.speedy = -abs(ball.speedy)
        ball.speedx=bar.speedx

    # ----- Gera saídas
    window.fill((0,0,0))
    # esta linha é para desenhar a barra
    window.blit(bar.image, bar.rect)
    # Adicione aqui o desenho da bola # adcionei
    window.blit(ball.image, ball.rect) 
    # ----- Desenhando bricks
    all_bricks.draw(window) 
    
    pygame.display.update() # mostra o novo frame para o jogador
#======Finalização=======
pygame.quit()






