#seção de configuração e definição de variáveis
import pygame
pygame.init()
LARGURA_TELA = 640
ALTURA_TELA = 480

#----------------------------------------------------

COR_AMARELA = (255, 255, 51)


#---------------------------------------------------

#cria o display (tela do jogo)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

#----------------------------------------------------
class Quadradinho:
    
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
        self.area = pygame.Rect(x, y, 50, 50)
    
    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)
        
q1 = Quadradinho(300,100, "green")
q2 = Quadradinho(350,300, "blue")

    
def escreve_msg(tela, texto, x, y):
        font = pygame.font.Font(None, 32)
        text = font.render(texto, False, COR_AMARELA)
        textpos = text.get_rect()
        textpos.center = (x, y)
        tela.blit(text, textpos)
        
escreve_msg(tela, "olá, infnet", 100, 100)  
    
terminou = False
while not terminou:
    #seção de tratamento de eevntod
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

#atualização de tela

    #atualização da tela do jogo
    pygame.display.update() 

#------ encerra a pygame ------
pygame.display.quit()
pygame.quit()

