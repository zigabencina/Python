import pygame

pygame.init()

screen_width = 800 
screen_height = 600

screen = pygame.display.set_mode((800,600))

color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)

font = pygame.font.SysFont('Corbel',35)

text = smallfont.render('quit' , True , color)

running = True

while running:
    ev = pygame.event.get()

    for event in ev:
        
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()