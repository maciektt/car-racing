import pygame


class Player:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.image = pygame.image.load("images/cars/car_blue.png")
        self.image = pygame.transform.scale(self.image, (75, 150))

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))