import pygame
#keys za prtisnt
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#inicializacija pygame-a
pygame.init()

#sirina screena
screen_width = 800  
#visina screena
screen_height = 600 

#funkcija za definiranje igralca kot objekt s tem d razširimoo pygame.sprite.Sprite
class Player(pygame.sprite.Sprite): 
    def __init__(self):   
        super(Player, self).__init__()
        #naredi surface za igralca
        self.surf = pygame.Surface((75, 25))
        #das surfaceu color in ga seperateas od backrounda
        self.surf.fill((255, 255, 255))
        #naredi rectangle za playerja
        self.rect = self.surf.get_rect()

#screen
screen = pygame.display.set_mode((screen_width,screen_height)) 

#narise krogc :O
pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

#var da se while loop konca k spremenimo na false
running = True    

#priklic class-a player
player = Player() 

#Main loop
while running:
    #ce prtisne close button se ugasne
    for event in pygame.event.get():
        #ce je event.type pritisnjen gumb   
        if event.type == KEYDOWN: 
            #in ce je event.key == escape
            if event.key == K_ESCAPE: 
                #naj se ugasne
                running = False 
        elif event.type == QUIT: 
            #ali ce je event.type == QUIT naj se tudi ugasne
            running = False
    
    #Bg color
    screen.fill((0, 0, 0)) 

    #Narise playerja na screen
    screen.blit(player.surf, (screen_width/2, screen_height/2)) 
   
    #Osvezi display
    pygame.display.flip()

#quita
pygame.quit()

