import pygame
from hanoi import *


pygame.init()
screen  = pygame.display.set_mode((1080, 720))
run = True

default_image_size = (200, 200)


fond = pygame.image.load('images musique/fond jeu hanoi.png').convert_alpha()
start_img = pygame.image.load("images musique/start_btn.png").convert_alpha()
tour_vide = pygame.image.load("images musique/tour vide_transparent.png").convert_alpha()
tour_1 = pygame.image.load("images musique/tour 1_transparent.png").convert_alpha()
tour_2 = pygame.image.load("images musique/tour 2_transparent.png").convert_alpha()
tour_3 = pygame.image.load("images musique/tour 3_transparent.png").convert_alpha()

_1_to_2 = pygame.image.load("images musique/1 to 2_transparent.png").convert_alpha()
_1_to_3 = pygame.image.load("images musique/1 to 3_transparent.png").convert_alpha()
_2_to_1 = pygame.image.load("images musique/2 to 1_transparent.png").convert_alpha()
_2_to_3 = pygame.image.load("images musique/2 to 3_transparent.png").convert_alpha()
_3_to_1= pygame.image.load("images musique/3 to 1_transparent.png").convert_alpha()
_3_to_2 = pygame.image.load("images musique/3 to 2_transparent.png").convert_alpha()


_1_to_2 = pygame.transform.scale(_1_to_2, (125, 75))
_1_to_3 = pygame.transform.scale(_1_to_3, (125, 50))

_2_to_1 = pygame.transform.scale(_2_to_1, (125, 50))
_2_to_3 = pygame.transform.scale(_2_to_3, (125, 50))

_3_to_1 = pygame.transform.scale(_3_to_1, (125, 50))
_3_to_2 = pygame.transform.scale(_3_to_2, (125, 50))


tour_vide = pygame.transform.scale(tour_vide, default_image_size)
tour_1 = pygame.transform.scale(tour_1, default_image_size)
tour_2 = pygame.transform.scale(tour_2, default_image_size)
tour_3 = pygame.transform.scale(tour_3, default_image_size)
fond = pygame.transform.scale(fond, (1080, 720))


class Tour(pygame.sprite.Sprite):
    def __init__(self, image, x, y) -> None:
        super().__init__()
        etat = 0
        self.image = image 
        self.x = x 
        self.y = y 
        
    def draw(self):
        screen.blit(self.image,( self.x, self.y))
            
        

class Button():
    def __init__(self, x, y, image):
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        #affiche le bouton sur l'ecrant 
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return action


    

screen.blit(fond,(0,0))
#creation boutton 
_1_to_2b = Button(75, 575, _1_to_2)
_1_to_3b = Button(75, 650, _1_to_3)

_2_to_1b = Button(475, 600, _2_to_1)
_2_to_3b = Button(475, 650, _2_to_3)

_3_to_1b = Button(850, 600, _3_to_1)
_3_to_2b = Button(850, 650, _3_to_2)


#creation graphisme 
a = 3
b = 0
c = 0

while run:
    if a == 0:
        tour1_img = tour_vide
        tour1 = Tour(tour1_img, 50, 350)
        tour1.draw()
    
    elif a == 1:
        tour1_img = tour_1
        tour1 = Tour(tour1_img, 50, 350)
        tour1.draw()
    
    elif a == 2:
        tour1_img = tour_2
        tour1 = Tour(tour1_img, 50, 350)
        tour1.draw()
    
    elif a == 3:
        tour1_img = tour_3
        tour1 = Tour(tour1_img, 50, 350)
        tour1.draw()
        
        
    if b == 0:
        tour2_img = tour_vide
        tour2 = Tour(tour2_img, 450, 125)
        tour2.draw()
    
    elif b == 1:
        tour2_img = tour_1
        tour2 = Tour(tour2_img, 450, 125)
        tour2.draw()
    
    elif b == 2:
        tour2_img = tour_2
        tour2 = Tour(tour2_img, 450, 125)
        tour2.draw()
    
    elif b == 3:
        tour2_img = tour_3
        tour2 = Tour(tour2_img, 450, 125)
        tour2.draw()



    if c == 0:
        tour3_img = tour_vide
        tour3 = Tour(tour3_img, 825, 350)
        tour3.draw()
    
    elif c == 1:
        tour3_img = tour_1
        tour3 = Tour(tour3_img, 825, 350)
        tour3.draw()
    
    elif c == 2:
        tour3_img = tour_2
        tour3 = Tour(tour3_img, 825, 350)
        tour3.draw()
    
    elif c == 3:
        tour3_img = tour_3
        tour3 = Tour(tour3_img, 825, 350)
        tour3.draw()

    
    
    
    
    
    
    
    
    
    
    
    
    if _1_to_2b.draw():
        a -= 1
        b += 1
    if _1_to_3b.draw():
        a -= 1
        c += 1
    
    if _2_to_1b.draw():
        a -= 1
        b += 1
    if _2_to_3b.draw():
        a -= 1
        c += 1
        
    if _3_to_1b.draw():
        a -= 1
        b += 1
    if _3_to_2b.draw():
        a -= 1
        c += 1
        


    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()