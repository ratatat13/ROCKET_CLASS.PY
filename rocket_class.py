import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
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


sprites = pygame.sprite.Group()

def start_game():
    rocket = player()
    sprites.add(rocket)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        pressed_keys = pygame.key.get_pressed 
        rocket.update(pressed_keys)
        screen.blit(pygame.image.load("space.png"), 0,0)
        sprites.draw(screen)
        pygame.display.update()

start_game()          