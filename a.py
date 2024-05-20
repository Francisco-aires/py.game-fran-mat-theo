#====== Inicialização=======

#---------- Importa e inicia pacotes
import pygame
import random

pygame.init()

#----------- importar outras coisas
#from funcoes import *

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

brick2_img=pygame.image.load('Img/07-Breakout-Tiles.png').convert_alpha()
brick2_img=pygame.transform.scale(brick2_img, (BRICK_WIDTH, BRICK_HEIGHT))

brick2_1_img=pygame.image.load('Img/08-Breakout-Tiles.png').convert_alpha()
brick2_1_img=pygame.transform.scale(brick2_1_img, (BRICK_WIDTH, BRICK_HEIGHT))

brick3_img=pygame.image.load('Img/05-Breakout-Tiles.png').convert_alpha()
brick3_img=pygame.transform.scale(brick3_img, (BRICK_WIDTH, BRICK_HEIGHT))

LIVE_WIDGTH = 20
LIVE_HEIGHT = 20
live_img = pygame.image.load('Img/60-Breakout-Tiles.png').convert_alpha()
live_img = pygame.transform.scale(live_img, (LIVE_WIDGTH, LIVE_HEIGHT))

BAR_WIDHTH=200
BAR_HEIGHT=25
bar_img=pygame.image.load('Img/17-Breakout-Tiles.png').convert_alpha()
bar_img = pygame.transform.scale(bar_img, (BAR_WIDHTH, BAR_HEIGHT))


BALL_WIDHTH=20
BALL_HEIGHT=20
ball_img=pygame.image.load('Img/58-Breakout-Tiles.png').convert_alpha()
ball_img=pygame.transform.scale(ball_img, (BALL_WIDHTH, BALL_HEIGHT))
POWER_WIDGTH = 30
POWER_HEIGHT = 30

BULLETS_WIDGTH = 10
BULLETS_HEIGHT = 20
bullets_img = pygame.image.load("Img/61-Breakout-Tiles.png")
bullets_img = pygame.transform.scale(bullets_img, (BULLETS_WIDGTH, BULLETS_HEIGHT))


CORACAO_WIDGHT=30
CORACAO_HEIGHT=30
coracao_img=pygame.image.load('Img/60-Breakout-Tiles.png').convert_alpha()
coracao_img=pygame.transform.scale(coracao_img, (CORACAO_WIDGHT,CORACAO_HEIGHT))

#imagens dos poderes
POWER_WIDTH = 40
POWER_HEIGHT = 30
#aumenta a barra
power_expand_bar_img = pygame.image.load('Img/47-Breakout-Tiles.png').convert_alpha()
power_expand_bar_img = pygame.transform.scale(power_expand_bar_img, (POWER_WIDTH, POWER_HEIGHT))
# extra vida
power_extra_life_img = pygame.image.load('Img/60-Breakout-Tiles.png').convert_alpha()
power_extra_life_img = pygame.transform.scale(power_extra_life_img, (POWER_WIDTH, POWER_HEIGHT))
# bola lenta
power_slow_ball_img = pygame.image.load('Img/41-Breakout-Tiles.png').convert_alpha()
power_slow_ball_img = pygame.transform.scale(power_slow_ball_img, (POWER_WIDTH, POWER_HEIGHT))
# bola rapida
power_fast_ball_img = pygame.image.load('Img/42-Breakout-Tiles.png').convert_alpha()
power_fast_ball_img = pygame.transform.scale(power_fast_ball_img, (POWER_WIDTH, POWER_HEIGHT))
#aumenta a barra
power_d_bar_img = pygame.image.load('Img/46-Breakout-Tiles.png').convert_alpha()
power_d_bar_img = pygame.transform.scale(power_d_bar_img, (POWER_WIDTH, POWER_HEIGHT))

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

# Funçao das colizôes
def check_collision(ball, brick):
    # Verifica a direção da bola
    ball_left = ball.rect.left
    ball_right = ball.rect.right
    ball_top = ball.rect.top
    ball_bottom = ball.rect.bottom
    ball_speedx = ball.speedx
    ball_speedy = ball.speedy

    brick_left = brick.rect.left
    brick_right = brick.rect.right
    brick_top = brick.rect.top
    brick_bottom = brick.rect.bottom

    # Calcula a interseção dos retângulos
    if ball_right > brick_left and ball_left < brick_right and ball_bottom > brick_top and ball_top < brick_bottom:
        # Calcula a profundidade da colisão em cada direção
        overlap_left = ball_right - brick_left
        overlap_right = brick_right - ball_left
        overlap_top = ball_bottom - brick_top
        overlap_bottom = brick_bottom - ball_top

        # Determina a direção da colisão
        if min(overlap_left, overlap_right) < min(overlap_top, overlap_bottom):
            # Colisão lateral
            if overlap_left < overlap_right:
                ball.rect.right = brick_left
            else:
                ball.rect.left = brick_right
            ball.speedx = -ball.speedx
        else:
            # Colisão superior ou inferior
            if overlap_top < overlap_bottom:
                ball.rect.bottom = brick_top
            else:
                ball.rect.top = brick_bottom
            ball.speedy = -ball.speedy

        return True
    return False



def tela_Gameover(window):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return "REINICIAR"

        window.fill((0, 0, 0))  # Define a cor de fundo da tela de Game Over
        font = pygame.font.Font(None, 36)  # Define a fonte

        # Cria um texto de Game Over
        texto_gameover = font.render('GAME OVER', True, ((255, 0, 0)))
        fim_rect = texto_gameover.get_rect(center=(WIDTH / 2, HEIGHT / 3))

        # Cria um texto de instrução
        instrucao = font.render('Pressione qualquer tecla para recomeçar', True, ((255, 255, 255)))
        instrucao_rect = instrucao.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        # Desenha os textos na tela
        window.blit(texto_gameover, fim_rect)
        window.blit(instrucao, instrucao_rect)

        pygame.display.update()

        
def tela_fim(window):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                running = False
                state = PLAYING

        window.fill((0, 0, 0))  # Define a cor de fundo da tela de início
        font = pygame.font.Font(None, 36)  # Define a fonte

        # Cria um texto de boas-vindas
        texto_inicio = font.render('Você ganhou!', True, ((255, 255, 255)))
        inicio_rect = texto_inicio.get_rect(center=(WIDTH / 2, HEIGHT / 3))

        # Cria um texto de instrução
        instrucao = font.render('Pressione qualquer tecla para recomeçar', True, ((255, 255, 255)))
        instrucao_rect = instrucao.get_rect(center=(WIDTH / 2, HEIGHT / 2))

        # Desenha os textos na tela
        window.blit(texto_inicio, inicio_rect)
        window.blit(instrucao, instrucao_rect)

def iniciar_jogo():
    global all_sprites, all_bricks, all_bricks_2, all_bricks_2_1, all_bricks_3
    global all_balls, all_powers, all_bullets, bar, ball, score, lives, state, FPS

    all_sprites = pygame.sprite.Group()
    all_bricks = pygame.sprite.Group()  # brick básico
    all_bricks_2 = pygame.sprite.Group()  # brick 2
    all_bricks_2_1 = pygame.sprite.Group()  # brick 2 meio quebrado quebrado
    all_bricks_3 = pygame.sprite.Group()  # brick 3(poder)
    all_balls = pygame.sprite.Group()
    all_powers = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()

    for i in range(30):
        brick = Brick(brick_img)
        all_bricks.add(brick)
        all_sprites.add(brick)
    for j in range(10):
        brick2 = Brick2(brick2_img)
        all_bricks_2.add(brick2)
        all_sprites.add(brick2)
    for m in range(10):
        brick3 = Brick3(brick3_img)
        all_bricks_3.add(brick3)
        all_sprites.add(brick3)

    bar = Bar(bar_img, WIDTH // 2, HEIGHT - 50)
    all_sprites.add(bar)

    ball = Ball(ball_img)
    all_sprites.add(ball)
    all_balls.add(ball)

    score = 0
    lives = 3
    FPS = 60
    state = "PLAYING"


############### carregar sons #####################
# Carrega o som de colisão
som_colisao = pygame.mixer.Sound('sons/somco.mp3')
#        som_colisao.play() se quiser tocar

# Carrega a música de fundo
pygame.mixer.music.load('sons/name.mp3')


#---------- Inicia estrutura de dados
#lista posições bricks
lista_x=[30,90,150,210,270,510,570,630,690,750]
lista_y=[30,60,90,120,180,210,240]
lista_bricks=[]#lista com a posição de todos os blocos

######################### poderessssss  ########################



class PowerUp(pygame.sprite.Sprite):
    def __init__(self, img, x, y, effect):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = 3  # Velocidade de queda do poder
        self.effect = effect  # Tipo de efeito do poder

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()



def apply_power(power):
    global bar, lives, ball
    power_duration = 300  # Duração do poder em frames (por exemplo, 5 segundos a 60 FPS)
    if power.effect == 'expand_bar':
        bar.image = pygame.transform.scale(bar.image, (BAR_WIDHTH * 1.5, BAR_HEIGHT))
        bar.rect = bar.image.get_rect(center=bar.rect.center)
        bar.power_timer = power_duration
    elif power.effect == 'extra_life':
        lives += 1
    elif power.effect == 'slow_ball':
        ball.speedx *= 0.8
        ball.speedy *= 0.5
        bar.power_timer = power_duration
    elif power.effect == 'fast_ball':
        ball.speedx *= 1.5
        ball.speedy *= 1.5
        bar.power_timer = power_duration
    elif power.effect == 'd_bar':
        bar.image = pygame.transform.scale(bar.image, (BAR_WIDHTH * 0.5, BAR_HEIGHT))
        bar.rect = bar.image.get_rect(center=bar.rect.center)
        bar.power_timer = power_duration



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


class Brick2(pygame.sprite.Sprite):
    def __init__(self,img):
        #Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        condicao=True
        while condicao:
            lista_par2=[] #lista com as coordenadas do brick para verificar se essa esta livre
            x= random.choice(lista_x)
            y=random.choice(lista_y)
            lista_par2.append(x)
            lista_par2.append(y)
            if lista_par2 in lista_bricks:   #Modificar caso já esteja lotado
                condicao=True
            else:
                condicao=False
                lista_bricks.append(lista_par2)
  
        self.rect.x = x
        self.rect.y = y
    # criar(função update(self)) se quiser movimentar o brick
    def update(self):
        self.rect.x=self.rect.x  #  ((compoletar função update))

class Brick2_1(pygame.sprite.Sprite):
    def __init__(self,img,x,y):
        #Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

  


class Brick3(pygame.sprite.Sprite):
    def __init__(self,img):
        #Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        condicao=True
        while condicao:
            lista_par3=[] #lista com as coordenadas do brick para verificar se essa esta livre
            x= random.choice(lista_x)
            y=random.choice(lista_y)
            lista_par3.append(x)
            lista_par3.append(y)
            if lista_par3 in lista_bricks:   #Modificar caso já esteja lotado
                condicao=True
            else:
                condicao=False
                lista_bricks.append(lista_par3)
  
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
            self.speedy=5
            self.speedx=0
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
        self.real_x = x
        self.power_timer = 0
        self.original_width = self.rect.width
        self.last_shot = pygame.time.get_ticks()  # Para controlar a cadência de tiro

    def update(self, keys):
        self.speedx = 0
        if keys[pygame.K_LEFT]:
            self.speedx = -7
        if keys[pygame.K_RIGHT]:
            self.speedx = 7
        self.real_x += self.speedx
        self.rect.x = int(self.real_x)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.real_x = self.rect.x
        if self.rect.left < 0:
            self.rect.left = 0
            self.real_x = self.rect.x

        # Verificar e atualizar o temporizador dos poderes
        if self.power_timer > 0:
            self.power_timer -= 1
        else:
            self.reset_powers()


    def reset_powers(self):
        self.image = pygame.transform.scale(bar_img, (self.original_width, BAR_HEIGHT))
        self.rect = self.image.get_rect(center=self.rect.center)



    


class Powers(pygame.sprite.Sprite):
    def __init__(self, dic_power_img, center, bottom):
        pygame.sprite.Sprite.__init__(self)
        self.power_type = random.choice(list(dic_power_img.keys()))
        self.image = dic_power_img[self.power_type]
        self.rect = self.image.get_rect()
        self.rect.centerx = center
        self.rect.bottom = bottom
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

    def power_up(self, dic_power_numeros):
        return dic_power_numeros[self.power_type]
   
class Timer:
    def __init__(self):
        self.power_timers = {}

    def update_powers(self):
        current_time = pygame.time.get_ticks()
        for power, end_time in list(self.power_timers.items()):
            if current_time > end_time:
                self.deactivate_power(power)
                del self.power_timers[power]

    def activate_power(self, power):
        current_time = pygame.time.get_ticks()
        duration = 5000  # Duração de 5 segundos para todos os poderes
        end_time = current_time + duration
        self.power_timers[power] = end_time

        if power == 41:
            self.FPS = 45
        elif power == 42:
            self.FPS = 75
        elif power == 43:
            for _ in range(2):
                ball = Ball(ball_img)  # Assumindo que você tem a imagem da bola definida
                all_sprites.add(ball)
                all_balls.add(ball)
        elif power == 44:
            pygame.sprite.groupcollide(all_balls, all_bricks_2, False, True, pygame.sprite.collide_mask)
        elif power == 45:
            pygame.sprite.groupcollide(all_balls, all_bricks, False, False, pygame.sprite.collide_mask)
        elif power == 46:
            self.BAR_WIDTH = 175
        elif power == 47:
            self.BAR_WIDTH = 225
        elif power == 48:
            brick_center = brick.rect.centerx  # Supondo que você tem o brick definido
            brick_bottom = brick.rect.bottom
            bullet = Bullets(bullets_img, brick_center, brick_bottom)  # Assumindo que você tem a imagem do bullet definida
            all_sprites.add(bullet)
            all_bullets.add(bullet)

    def deactivate_power(self, power):
        if power == 41 or power == 42:
            self.FPS = 60
        elif power == 43:
            while len(all_balls) > 1:
                ball = all_balls.sprites()[0]
                ball.kill()
        elif power == 44 or power == 45:
            pygame.sprite.groupcollide(all_balls, all_bricks_2, False, False, pygame.sprite.collide_mask)
        elif power == 46 or power == 47:
            self.BAR_WIDTH = 200
        elif power == 48:
            for bullet in all_bullets:
                bullet.kill()


                    
class Bullets(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -1  # Velocidade fixa para cima

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()




game=True

#criando grupo Bricks
all_sprites = pygame.sprite.Group()
all_bricks=pygame.sprite.Group() #brick básico
all_bricks_2=pygame.sprite.Group() #brick 2
all_bricks_2_1=pygame.sprite.Group() #brick 2 meio quebrado quebrado
all_bricks_3=pygame.sprite.Group() #brick 3(poder)
all_balls=pygame.sprite.Group()
all_powers = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()


tela_inicio(window)

# Inicia a reprodução da música de fundo em loop
pygame.mixer.music.play(-1)

# Variável que ajusta velocidde[
clock = pygame.time.Clock()
FPS = 60

DONE = 0
PLAYING = 1
GAMEOVER = 2

state = PLAYING

condicao_jogo=0

lives=3
score = 0
#========loop principal========
while condicao_jogo<3:
    lista_bricks=[]
    
    if state==GAMEOVER:
        state=PLAYING
        lives=3
        score=0
        all_sprites.empty()
        all_bricks.empty()
        all_bricks_2.empty()
        all_bricks_2_1.empty()
        all_bricks_3.empty()
        all_balls.empty()
  
        
            #Barrinha criada
    bar = Bar(bar_img, WIDTH // 2, HEIGHT - 50) 
    all_sprites.add(bar)

    condicao_hit_ball_bar=0

    #bolinhaaaaaaaaaaaaaa
    ball = Ball(ball_img)
    all_sprites.add(ball)
    all_balls.add(ball)
   
    for i in range(30):
        brick=Brick(brick_img)
        all_bricks.add(brick)
        all_sprites.add(brick)


    for j in range(10):
        brick2=Brick2(brick2_img)
        all_bricks_2.add(brick2)
        all_sprites.add(brick2)


    for m in range(10):
        brick3=Brick3(brick3_img)
        all_bricks_3.add(brick3)
        all_sprites.add(brick3)

    while state!=DONE and state!=GAMEOVER:

        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
                condicao_jogo=5

        # Captura as teclas pressionadas uma vez por frame
        keys = pygame.key.get_pressed()

        # ----- Atualiza estado de jogo

        #atualiza posições (barra e bola)
        all_bricks.update()  # os tijolos se movam ou tenham alguma atualização
        all_bricks_2.update()
        all_bricks_2_1.update()
        all_bricks_3.update()
        bar.update(keys) # Atualiza a posição da barra com base nas entradas do teclado
        ball.update() #bolinha movendoo
        all_powers.update()
        #verifica se houve colisão
        # colizao da bolinha X bloco
        
        hits_ball_brick = pygame.sprite.groupcollide(all_balls, all_bricks, False, True, pygame.sprite.collide_mask)
        for ball, bricks_hit in hits_ball_brick.items():
            for brick in bricks_hit:
                if check_collision(ball, brick):
                    score += 100
        
        hits_ball_brick2 = pygame.sprite.groupcollide(all_balls, all_bricks_2, False, True, pygame.sprite.collide_mask)
        for ball, bricks2_hit in hits_ball_brick2.items():
            for brick in bricks2_hit:
                if check_collision(ball, brick):
                    score += 200
                    brick_2_1 = Brick2_1(brick2_1_img, brick.rect.x, brick.rect.y)
                    all_bricks_2_1.add(brick_2_1)
                    all_sprites.add(brick_2_1)
            
            

        hits_ball_brick3 = pygame.sprite.groupcollide(all_balls, all_bricks_3, False, True, pygame.sprite.collide_mask)
        for ball, bricks_hit3 in hits_ball_brick3.items():
            for brick in bricks_hit3:
                if check_collision(ball, brick):
                    score += 100
                    power_type = random.choice(['expand_bar', 'extra_life', 'slow_ball', 'fast_ball','d_bar'])
                    if power_type == 'expand_bar':
                        power = PowerUp(power_expand_bar_img, brick.rect.x, brick.rect.y, 'expand_bar')
                    elif power_type == 'extra_life':
                        power = PowerUp(power_extra_life_img, brick.rect.x, brick.rect.y, 'extra_life')
                    elif power_type == 'slow_ball':
                        power = PowerUp(power_slow_ball_img, brick.rect.x, brick.rect.y, 'slow_ball')
                    elif power_type == 'fast_ball':
                        power = PowerUp(power_fast_ball_img, brick.rect.x, brick.rect.y, 'fast_ball')
                    elif power_type == 'd_bar':
                        power = PowerUp(power_d_bar_img , brick.rect.x, brick.rect.y, 'd_bar')
                    all_powers.add(power)
                    all_sprites.add(power)


        hits_ball_brick_2_1 = pygame.sprite.groupcollide(all_balls, all_bricks_2_1, False, True, pygame.sprite.collide_mask)
        for ball, bricks_hit in hits_ball_brick_2_1.items():
            for brick in bricks_hit:
                if check_collision(ball, brick):
                    score += 200

        # colizao do poder
        hits_power_bar = pygame.sprite.spritecollide(bar, all_powers, True, pygame.sprite.collide_mask)
        for power in hits_power_bar:
            apply_power(power)
                    
        

        # colizao da barrinha X bolinha
        hits_ball_bar=pygame.sprite.spritecollide(bar,all_balls,False,pygame.sprite.collide_mask)

        if len(hits_ball_bar)>ball.condicao_hit_ball_bar:
            ball.speedy = -abs(ball.speedy)
            if ball.speedx>0:
                if bar.speedx > 0:
                    ball.speedx = bar.speedx
                elif bar.speedx < 0:
                    ball.speedx=ball.speedx+bar.speedx+2
                else:
                    ball.speedx = ball.speedx
            elif ball.speedx<0:
                if bar.speedx < 0:
                    ball.speedx = bar.speedx
                elif bar.speedx > 0:
                    ball.speedx=ball.speedx+bar.speedx-2
                else:
                    ball.speedx = ball.speedx
            elif ball.speedx==0:
                if bar.speedx < 0:
                    ball.speedx = bar.speedx
                elif bar.speedx > 0:
                    ball.speedx= bar.speedx
                else:
                    ball.speedx = ball.speedx


        if ball.rect.bottom >= HEIGHT: 
            lives-=1

        # ----- Gera saídas
        window.fill((0,0,0))
        # esta linha é para desenhar a barra
        window.blit(bar.image, bar.rect)
        # Adicione aqui o desenho da bola # adcionei
        window.blit(ball.image, ball.rect) 
        # ----- Desenhando bricks
        all_bricks.draw(window)

        all_bricks_2.draw(window)

        all_bricks_2_1.draw(window)

        all_bricks_3.draw(window)

        all_powers.draw(window)


        # Desenhando as vidas
        font = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
        text_surface =font.render(chr(9829) * lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)
        # desenhando a pontuação
        text_surface = pygame.font.Font('assets/font/PressStart2P.ttf', 24).render("{:08d}".format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)
        
        pygame.display.update() # mostra o novo frame para o jogador

        if lives==0:
            state = GAMEOVER
            if tela_Gameover(window) != "REINICIAR":
                condicao_jogo=5
#======Finalização=======
pygame.quit()