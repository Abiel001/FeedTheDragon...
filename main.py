import pygame

#set display surface
pygame.init()

#set display surface
WINDOW_WIDTH = 100
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("feed the dragon")

''' we will write more code here '''

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.quit()