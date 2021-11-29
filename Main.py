import pygame
import random
from Enviroment import *
from Player import *
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WIDTH = 480
HEIGHT = 600
FPS = 60
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shumerian nights")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
inv=Inventory()
player1=pygame.sprite.Group()
player1.add(player)
inv1=pygame.sprite.Group()
items=pygame.sprite.Group()
for i in range (30):
    it=Item_inv(inv,i)
    items.add(it)
inv1.add(inv)
tree=env_object(100,200)
house=env_object(300,100)
all_sprites.add(tree)
all_sprites.add(house)
running = True
collide=list()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update(collide)
    all_sprites.update(player)
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_e]:
        player.open_inv(inv,items)
    if keystate[pygame.K_ESCAPE]:
        player.close_inv(inv,items)
    collide=pygame.sprite.groupcollide(player1,all_sprites,False,False)
    screen.fill(WHITE)
    all_sprites.draw(screen)
    player1.draw(screen)
    inv1.draw(screen)
    items.draw(screen)
    pygame.display.flip()
pygame.quit()