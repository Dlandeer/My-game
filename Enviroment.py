import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WIDTH = 480
HEIGHT = 600
FPS = 60
class env_object(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 60))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.gx=x
        self.gy=y

    def update(self,Player):
        self.rect.x-=Player.speedx
        self.rect.y-=Player.speedy
           
        
