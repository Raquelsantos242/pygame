#seção de configuração e definição de variáveis
import pygame
pygame.init()
LARGURA_TELA = 640
ALTURA_TELA = 480

#cria o display (tela do jogo)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))



#seção game loop
terminou = False
while not terminou:
    #seção de tratamento de eevntod
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            tela.fill((255,255,255))
            
            if event.button == 1:#circulo azul de raio 100 no centro
                pygame.draw.circle(tela, "blue", (320, 240), 100)
            elif event.button == 3:#quadrado vermelho, lado 200, no centro
                pygame.draw.rect(tela, "red", (220, 140, 200, 200))
    #atualização da tela do jogo
    pygame.display.update() 

#------ encerra a pygame ------
pygame.display.quit()
pygame.quit()