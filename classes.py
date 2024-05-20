#imports
import time
import pygame
import random

from funcoes import *
###########
# classes #
###########

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
