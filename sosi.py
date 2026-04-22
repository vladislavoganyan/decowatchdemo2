import random

import pygame
pygame.init()
FPS = 120
clock = pygame.time.Clock()
dlina = 800
shirina = 500
background = pygame.image.load("zelti.jpg")
zemla = pygame.image.load("zemla.png")
background = pygame.transform.scale(background, (dlina, shirina))
zemla = pygame.transform.scale(zemla, (900, 100))
amoznonakulakax = pygame.display.set_mode((dlina, shirina))
scroll_speed = 1.5
ground_scroll = 0

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("птица хуйня/1.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.images = []
        for num in range(1, 13):
            img = pygame.image.load("птица хуйня/%s.png" % num)
            self.images.append(img)
        self.index = 0
        self.counter = 0
    def update(self):
        self.counter += 0
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        self.image = pygame.transform.flip(self.image, True, False)
bird = Bird(100, dlina // 2)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    amoznonakulakax.blit(background,(0, 0))
    amoznonakulakax.blit(zemla, (ground_scroll, 400))
    amoznonakulakax.blit(bird.image, bird.rect)
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 75.6:
        ground_scroll = 0
    pygame.display.flip()
    bird.update()