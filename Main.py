import pygame
import random
from Classes import *
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
player1=pygame.sprite.Group()
player1.add(player)
tree=env_object(100,200)
house=env_object(300,100)
all_sprites.add(tree)
all_sprites.add(house)
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update(player)
    player.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    player1.draw(screen)
    pygame.display.flip()

pygame.quit()