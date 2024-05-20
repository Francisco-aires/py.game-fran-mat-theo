#imports
import time
import pygame
import random

from assets import *
###########
# funções #
###########

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