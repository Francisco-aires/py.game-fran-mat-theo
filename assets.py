#imports
import time
import pygame
import random

###########
# assets  #
###########

WIDTH=850
HEIGHT=600
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('BREAKOUT INSPER')


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