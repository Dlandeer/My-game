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
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.gx = WIDTH/2
        self.gy = HEIGHT/2
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2-25
        self.rect.y = HEIGHT/2-20
        self.speedx = 0
        self.speedy = 0
    def update(self,collide):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.speedy=-8
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.speedy=8
        if collide:
            self.speedy=-self.speedy
            self.speedx=-self.speedx
        self.gx+=self.speedx
        self.gy+=self.speedy
    def open_inv(self,inv,inv_o):
        inv.update()
        inv_o.update()
    def close_inv(self,inv,inv_o):
        inv.disupdate()
        inv_o.update()
class Inventory(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 200))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=10000
        self.rect.y=10000
    def update(self):
        self.rect.x= WIDTH/2-150
        self.rect.y= HEIGHT/2-100
    def disupdate(self):
        self.rect.x=10000
        self.rect.y=10000
class Item_inv(pygame.sprite.Sprite):
    def __init__(self,inv,i):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.inv=inv
        self.i=i
        self.rect.x=inv.rect.x
        self.rect.y=inv.rect.y
    def update(self):
        self.rect.x=self.inv.rect.x + (self.i//7)*40
        self.rect.y=self.inv.rect.y+(self.i - (self.i//7)*7)*30
