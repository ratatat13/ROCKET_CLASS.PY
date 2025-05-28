import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((600,600))
screen.fill((255,23,255))
pygame.display.update()
pygame.display.set_caption("my own rocket")

class player(pygame.sprite.Sprite):
    def __init__ (self):
        self.image = pygame.image.load("rocket.png")
        self.image = pygame.image.load("space.png")
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys(pygame.K_UP):
            self.rect.move(0, -5)
        if pressed_keys(pygame.K_DOWN):
            self.rect.move(0, 5)
        if pressed_keys(pygame.K_LEFT):
            self.rect.move(-5, 0)
        if pressed_keys(pygame.K_RIGHT):
            self.rect.move(5, 0)

        if self.rect.left<0:
            self.rect.left = 0
            
        if self.rect.right>WIDTH:
            self.rect.right = WIDTH

        if self.rect.top<= 0:
            self.rect.top = 0

        if self.rect.bottom>= HEIGHT:
            self.rect.bottom = HEIGHT