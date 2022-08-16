#seção de configuração e definição de variáveis
import pygame
pygame.init()
LARGURA_TELA = 640
ALTURA_TELA = 480

#cria o display (tela do jogo)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

pygame.draw.rect(tela, "cyan", (20, 30, 150, 50), 5) #desenha retangulo

pygame.draw.circle(tela, "green", (300, 250), 75, 2)#desenha circulo

#seção game loop
terminou = False
while not terminou:
    #seção de tratamento de eevntod
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    #atualização da tela do jogo
    pygame.display.update() 

#------ encerra a pygame ------
pygame.display.quit()
pygame.quit()