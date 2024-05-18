#====== Inicialização=======

#---------- Importa e inicia pacotes
import pygame
import random

pygame.init()

#----------- importar outras coisas


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

BAR_WIDHTH=200
BAR_HEIGHT=25
bar_img=pygame.image.load('Img/17-Breakout-Tiles.png').convert_alpha()
bar_img = pygame.transform.scale(bar_img, (BAR_WIDHTH, BAR_HEIGHT))


BALL_WIDHTH=20
BALL_HEIGHT=20
ball_img=pygame.image.load('Img/58-Breakout-Tiles.png').convert_alpha()
ball_img=pygame.transform.scale(ball_img, (BALL_WIDHTH, BALL_HEIGHT))
POWER_WIDGTH = 20
POWER_HEIGHT = 20
dic_power_image = {}
dic_power_numeros = {}
for i in range(41, 49):
    dic_power_image["Poder {0}".format(i)] = pygame.image.load('Img/{0}-Breakout-Tiles.png'.format(i)).convert_alpha()
    dic_power_image["Poder {0}".format(i)] = pygame.transform.scale(dic_power_image["Poder {0}".format(i)], (POWER_WIDGTH, POWER_HEIGHT))
    dic_power_numeros["Poder {0}".format(i)] = i
BULLETS_WIDGTH = 10
BULLETS_HEIGHT = 20
bullets_img = pygame.image.load("Img/61-Breakout-Tiles.png")
bullets_img = pygame.transform.scale(bullets_img, (BULLETS_WIDGTH, BULLETS_HEIGHT))
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

def tela_Gameover(window):
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
            self.speedx = -7
        if keys[pygame.K_RIGHT]:
            self.speedx = 7
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
    def __init__(self, dic_power_img, center, bottom):
        pygame.sprite.Sprite.__init__(self)
        escolha = random.choice(dic_power_img) # Escolhe qual dos poderes será usado
        self.image = dic_power_image[escolha]
        self.rect = self.image.get_rect()
        self.rect.centerx = center
        self.rect.bottom = bottom
        self.speedy = 5
    def update(self):
        self.rect.y += self.speedy # Atualiza o poder com sua velocidade padrão
        if self.rect.bottom < 0:
            self.kill() # Apaga o sprite do poder caso ele saia da tela

    def power_up(self, dic_power_numbers):
        power = dic_power_numbers[self.image] # Acha qual é o poder dependendo de qual imagem foi escolhida
        inicial = pygame.time.get_ticks()
        self.frame_ticks = 5000
        if power == 41:
            FPS = 45 # Poder que deixa o jogo mais lento
        if power == 42:
            FPS = 75 # Poder que deixa o jogo mais rápido
        if power == 43:
            for i in range(2):
                ball = Ball(ball_img) # Poder que adiciona mais duas bolas ao jogo
                all_sprites.add(ball)
                all_balls.add(ball)
        if power == 44:
            pygame.sprite.groupcollide(all_balls, all_bricks, False, True, pygame.sprite.collide_mask) # Poder que deixa a bola forte           
        if power == 45:
            pygame.sprite.groupcollide(all_balls, all_bricks, False, False, pygame.sprite.collide_mask) # Poder que deixa a bola fraca
        if power == 46: 
            BAR_WIDHTH = 175 # Poder que diminui a barra
        if power == 47:
            BAR_WIDHTH = 225 # Poder que expande a barra
        if power == 48:
            bullets = Bullets(bullets_img, bar.centerx, bar.bottom)
            all_sprites.add(bullets)
            all_bullets.add(bullets)
class Bullets(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()




game=True

#criando grupo Bricks
all_sprites = pygame.sprite.Group()
all_bricks=pygame.sprite.Group() #brick básico
all_bricks_2=pygame.sprite.Group() #brick 2
all_bricks_2_1=pygame.sprite.Group() #brick 2 meio quebrado quebrado
all_balls=pygame.sprite.Group()
all_powers = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

#Criando os Bricks
for i in range(100):
    brick=Brick(brick_img)
    all_bricks.add(brick)
    all_sprites.add(brick)

for j in range(1):
    brick2=Brick(brick2_img)
    all_bricks_2.add(brick2)
    all_sprites.add(brick2)

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
    all_bricks_2.update()
    all_bricks_2_1.update()
    bar.update(keys) # Atualiza a posição da barra com base nas entradas do teclado
    ball.update() #bolinha movendoo
    #verifica se houve colisão
    # colizao da bolinha X bloco
    hits_ball_brick=pygame.sprite.groupcollide(all_balls, all_bricks, False, True, pygame.sprite.collide_mask)
   
    # colizao com o bloco inverte a bola
    for ball, bricks_hit in hits_ball_brick.items():
        ball_left=ball.rect.left
        ball_right=ball.rect.right
        ball_top=ball.rect.top
        ball_bottom=ball.rect.bottom
        ball_speedx=ball.speedx
        ball_speedy=ball.speedy
        for brick in bricks_hit:
            
            brick_left=brick.rect.left
            brick_right=brick.rect.right
            brick_top=brick.rect.top
            brick_bottom=brick.rect.bottom

            
         

            #verifia se a colisão foi diferente
            if ball_left>=brick_left and ball_right<=brick_right: #Colisão em baixo ou em cima
                # A colisão é mais provavelmente superior ou inferior
                ball.speedy = -ball.speedy
            elif ball_bottom<=brick_bottom and ball_top>=brick_top:
                # A colisão é mais provavelmente lateral
                ball.speedx = -ball.speedx
            else:
                if ball_speedx>0 and ball_speedy<0:
                    print('entrou')
                    if ball_right<brick_left+ball.rect.width and ball_top>brick_bottom-ball.rect.height:
                        print('caiu')
                        ball.speedy = -ball.speedy
                        ball.speedx = -ball.speedx
                    elif ball_left>brick_right-ball.rect.width and ball_top>brick_bottom-ball.rect.height:
                        print('caiu')
                        ball.speedy=-ball.speedy
                
                    elif ball_right<brick_left+ball.rect.width and ball_bottom<brick_top+ball.rect.height:
                        print('caiu')
                        ball.speedx=-ball.speedx
                    else:
                        print('não caiu')

                elif ball_speedx<0 and ball_speedy>0:
                    if ball_left>brick_right+ball.rect.width and ball_top>brick_bottom-ball.rect.height:
                        ball.speedx=-ball.speedx
                
                    elif ball_right<brick_left+ball.rect.width and ball_bottom<brick_top+ball.rect.height:
                        ball.speedy=-ball.speedy

                    elif ball_left>brick_right-ball.rect.width and ball_bottom<brick_top+ball.rect.height:
                        ball.speedx=-ball.speedx
                        ball.speedy = -ball.speedy

                elif ball_speedx<0 and ball_speedy<0:
                    if ball_right<brick_left+ball.rect.width and ball_top>brick_bottom-ball.rect.height:
                        ball.speedy = -ball.speedy

                    elif ball_left>brick_right-ball.rect.width and ball_top>brick_bottom-ball.rect.height:
                        ball.speedx=-ball.speedx
                        ball.speedy = -ball.speedy

                    elif ball_left>brick_right-ball.rect.width and ball_bottom<brick_top+ball.rect.height:
                        ball.speedx=-ball.speedx
                
                elif ball_speedx>0 and ball_speedy>0:
                    if ball_right<brick_left+ball.rect.width and ball_top>brick_bottom-ball.rect.height:
                        ball.speedx = -ball.speedx

                
                    elif ball_right<brick_left+ball.rect.width and ball_bottom<brick_top+ball.rect.height:
                        ball.speedy=-ball.speedy
                        ball.speedx=-ball.speedx

                    elif ball_left>brick_right-ball.rect.width and ball_bottom<brick_top+ball.rect.height:
                        ball.speedy=-ball.speedy

                   

            ('''brick=bricks_hit[1]

        #verifia se a colisão foi diferente
        if ball_left>=brick_left and ball_right<=brick_right: #Colisão em baixo ou em cima
                # A colisão é mais provavelmente superior ou inferior
                ball.speedy = -ball.speedy
        elif ball_bottom<=brick_bottom and ball_top>=brick_top:
            # A colisão é mais provavelmente lateral
            ball.speedx = -ball.speedx
        else:
            if ball.speedx>=0 and ball.speedy<=0:
                if ball_right<=brick_left and ball_top>=brick_bottom:
                    ball.speedy = -ball.speedy
                    ball.speedx = -ball.speedx
                elif ball_left>=brick_right and ball_top>=brick_bottom:
                    ball.speedy=-ball.speedy
            
                elif ball_right<=brick_left and ball_bottom<=brick_top:
                    ball.speedx=-ball.speedx

                elif ball_left>=brick_right and ball_bottom<=brick_top:###
                    ball.speedx=-ball.speedx 
                    ball.speedy = -ball.speedy

            elif ball.speedx<=0 and ball.speedy>=0:
                if ball_right<=brick_left and ball_top>=brick_bottom:###
                    ball.speedy = -ball.speedy
                    ball.speedx = -ball.speedx
                elif ball_left>=brick_right and ball_top>=brick_bottom:
                    ball.speedx=-ball.speedx
            
                elif ball_right<=brick_left and ball_bottom<=brick_top:
                    ball.speedy=-ball.speedy

                elif ball_left>=brick_right and ball_bottom<=brick_top:
                    ball.speedx=-ball.speedx
                    ball.speedy = -ball.speedy

            elif ball.speedx<=0 and ball.speedy<=0:
                if ball_right<=brick_left and ball_top>=brick_bottom:
                    ball.speedy = -ball.speedy

                elif ball_left>=brick_right and ball_top>=brick_bottom:
                    ball.speedx=-ball.speedx
                    ball.speedy = -ball.speedy
            
                elif ball_right<=brick_left and ball_bottom<=brick_top:###
                    ball.speedy=-ball.speedy
                    ball.speedx=-ball.speedx

                elif ball_left>=brick_right and ball_bottom<=brick_top:
                    ball.speedx=-ball.speedx
            
            elif ball.speedx>=0 and ball.speedy>=0:
                if ball_right<=brick_left and ball_top>=brick_bottom:
                    ball.speedx = -ball.speedx

                elif ball_left>=brick_right and ball_top>=brick_bottom:###
                    ball.speedx=-ball.speedx
                    ball.speedy = -ball.speedy
            
                elif ball_right<=brick_left and ball_bottom<=brick_top:
                    ball.speedy=-ball.speedy
                    ball.speedx=-ball.speedx

                elif ball_left>=brick_right and ball_bottom<=brick_top:
                    ball.speedy=-ball.speedy ''')
        

    

    hits_ball_brick2=pygame.sprite.groupcollide(all_balls, all_bricks_2, False, False, pygame.sprite.collide_mask)
    ball_center = ball.rect.centerx
    brick2_center = brick2.rect.centerx

    for ball, bricks2_hit in hits_ball_brick2.items():
        if len(bricks2_hit)==1:
            brick2 = bricks2_hit[0]  # Pega o primeiro tijolo atingido
            if abs(ball_center - brick2_center) <= brick2.rect.width / 2:
                # A colisão é mais provavelmente superior ou inferior
                ball.speedy = -ball.speedy
            else:
                # A colisão é mais provavelmente lateral
                ball.speedx = -ball.speedx
            
            # Verifica se a colisão foi mais lateral do que superior/inferior
            # Comparando o centro da bola com o centro do tijolo
            ball_center = ball.rect.centerx
            brick2_center = brick2.rect.centerx

            # Verifica se a colisão foi mais lateral
            if abs(ball_center - brick2_center) <= brick2.rect.width / 2:
                # A colisão é mais provavelmente superior ou inferior
                ball.speedy = -ball.speedy
        
            else:
                # A colisão é mais provavelmente lateral
                ball.speedx = -ball.speedx

            
        if len(bricks2_hit)==2:
            brick2 =bricks2_hit[0]
            ball_center = ball.rect.centerx
            brick2_center = brick2.rect.centerx
            

            #verifia se a colisão foi diferente
            if abs(ball_center - brick2_center) <= brick2.rect.width / 2:
                # A colisão é mais provavelmente superior ou inferior
                ball.speedy = -ball.speedy
            else:
                # A colisão é mais provavelmente lateral
                ball.speedx = -ball.speedx
            brick2=bricks2_hit[1]

            # Verifica se a colisão foi mais lateral do que superior/inferior
            # Comparando o centro da bola com o centro do tijolo
            ball_center = ball.rect.centerx
            brick2_center = brick2.rect.centerx

            # Verifica se a colisão foi mais lateral
            if abs(ball_center - brick2_center) <= brick2.rect.width / 2:
                # A colisão é mais provavelmente superior ou inferior
                ball.speedy = -ball.speedy
        
            else:
                # A colisão é mais provavelmente lateral
                ball.speedx = -ball.speedx
            
        for brick2 in bricks2_hit:
            brick2=Brick(brick2_1_img)
            all_bricks_2_1.add(brick2)
            all_bricks_2.remove(brick2)
        
    hits_ball_brick2_1=pygame.sprite.groupcollide(all_balls, all_bricks_2_1, False, True, pygame.sprite.collide_mask)
    for ball, bricks2_1_hit in hits_ball_brick2.items():
        if len(bricks2_1_hit)==1:
            brick = bricks2_1_hit[0]  # Pega o primeiro tijolo atingido
           
            

            
        if len(bricks2_1_hit)==2:
            brick=bricks2_1_hit[0]
            ball_center = ball.rect.centerx
            brick_center = brick.rect.centerx
            

            #verifia se a colisão foi diferente
            if abs(ball_center - brick_center) <= brick.rect.width / 2:
                # A colisão é mais provavelmente superior ou inferior
                ball.speedy = -ball.speedy
            else:
                # A colisão é mais provavelmente lateral
                ball.speedx = -ball.speedx
            brick=bricks2_1_hit[1]

            # Verifica se a colisão foi mais lateral do que superior/inferior
            # Comparando o centro da bola com o centro do tijolo
            ball_center = ball.rect.centerx
            brick_center = brick.rect.centerx

            # Verifica se a colisão foi mais lateral
            if abs(ball_center - brick_center) <= brick.rect.width / 2:
                # A colisão é mais provavelmente superior ou inferior
                ball.speedy = -ball.speedy
        
            else:
                # A colisão é mais provavelmente lateral
                ball.speedx = -ball.speedx
        

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

        

    # ----- Gera saídas
    window.fill((0,0,0))
    # esta linha é para desenhar a barra
    window.blit(bar.image, bar.rect)
    # Adicione aqui o desenho da bola # adcionei
    window.blit(ball.image, ball.rect) 
    # ----- Desenhando bricks
    all_bricks.draw(window)

    all_bricks_2.draw(window)
    
    pygame.display.update() # mostra o novo frame para o jogador
#======Finalização=======
pygame.quit()
