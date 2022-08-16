#seção de configuração e definição de variáveis
import pygame
pygame.init()
LARGURA_TELA = 640
ALTURA_TELA = 480

#----------------------------------------------------
clock = pygame.time.Clock() #cria o relógio do jogo
FPS = 50
COR_AMARELA = (255, 255, 51)
COR_PRETA = (0, 0, 0)
lado = 50; x = 0; y = 100;

#---------------------------------------------------

#cria o display (tela do jogo)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

#----------------------------------------------------
def desenha_quadrado_amarelo(tela, x, y, lado):
    pygame.draw.rect(tela, COR_AMARELA, (x, y, lado, lado))

#seção game loop
terminou = False
while not terminou:
    #seção de tratamento de eevntod
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
#---------------------animação de quadrado------------------------
    tela.fill(COR_PRETA)
    desenha_quadrado_amarelo(tela, x, y, lado)
    if (x < LARGURA_TELA - lado):
        x += 5
    
            
#atualização de tela
    clock.tick(FPS)
    #atualização da tela do jogo
    pygame.display.update() 

#------ encerra a pygame ------
pygame.display.quit()
pygame.quit()
