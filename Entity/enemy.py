import pygame


class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.is_moving = True
        self.image = pygame.image.load("images/cars/car_orange.png")
        self.image = pygame.transform.scale(self.image, (75, 150))
        self.image = pygame.transform.rotate(self.image,180)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self):
        if self.is_moving:
            self.y += 10