import pygame
import sys
import random

from Entity.player import Player
from Entity.enemy import Enemy

pygame.init()

width, height = 850, 720
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Moja gra")

player = Player()
enemies = []

clock = pygame.time.Clock()
spawn_timer = 0

image = pygame.image.load("images/road_f.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    elapsed_time = pygame.time.get_ticks() - spawn_timer
    if elapsed_time >= 1000:
        spawn_timer = pygame.time.get_ticks()
        enemy = Enemy(random.randint(20,620), -150)
        enemies.append(enemy)

    keys = pygame.key.get_pressed()
    speed = 5
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_SPACE]:
        player.y += -10

    window.fill((22, 221, 252))
    window.blit(image,(0,0))

    player.draw(window)
    for e in enemies:
        e.draw(window)
        e.move()



    pygame.display.flip()

    pygame.time.Clock().tick(60)