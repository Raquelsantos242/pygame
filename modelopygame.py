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
            
     pygame.display.update() 

#------ encerra a pygame ------
pygame.display.quit()
pygame.quit()