#imports
import time
import pygame
import random
###########
# funções #
###########

#contagem regressiva
def contagem_regressiva(tempo):
    for i in range(tempo, 0, -1):
        print(i)
        time.sleep(1)

#tela de inicio
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

