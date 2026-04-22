import random

import pygame

pygame.init()
FPS = 120
clock = pygame.time.Clock()
dlina = 600
shirina = 600
run = True
amoznonakulakax = pygame.display.set_mode((dlina, shirina))
background = pygame.image.load("abasralis.jpg")
background = pygame.transform.scale(background, (dlina, shirina))

class Gameobject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, dlina, shirina):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (dlina, shirina))
        self.rect = self.image.get_rect(center=(x, y))

class Spike(Gameobject):
    def __init__(self, x, y):
        super().__init__(x, y, "idi.jpeg", 100, 100)
    def ahh(self):
        self.rect.x = random.randint(100, 500)
        self.rect.y = random.randint(100, 500)


class Seregapirat(Gameobject):
    def __init__(self, x, y):
        super().__init__(x, y, "виталя.jpg", 50, 50)
    def zanovo(self):
        self.rect.x = random.randint(100, 500)
        self.rect.y = random.randint(100, 500)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("deko.jpg")
        self.visota = 100
        self.pusiko = 100
        self.speedx = 0
        self.speedy = 0
        self.image = pygame.transform.scale(self.image, (self.visota, self.pusiko))
        self.rect = self.image.get_rect(center=(x, y))
        self.vitalik = 0

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


player = Player(100, 100)
spikes = [Spike(random.randint(210, 500), random.randint(210, 500)), Spike(random.randint(210, 500), random.randint(210, 500))]
lagushka = [Seregapirat(random.randint(0, 500), random.randint(0, 500))]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and shirina - player.visota > player.rect.x:
                player.speedx += 2
            if event.key == pygame.K_a and player.rect.x > 0:
                player.speedx -= 2
            if event.key == pygame.K_w and player.rect.y > 0:
                player.speedy -= 2
            if event.key == pygame.K_s and shirina - player.visota > player.rect.y:
                player.speedy += 2
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                player.speedx = 0
            if event.key in (pygame.K_w, pygame.K_s):
                player.speedy = 0

    player.move()

    amoznonakulakax.blit(background, (0, 0))

    for spike in spikes:
        amoznonakulakax.blit(spike.image, (spike.rect.x, spike.rect.y))
        if player.rect.colliderect(spike.rect):
            run = False
    for lagushkas in lagushka:
        amoznonakulakax.blit(lagushkas.image, (lagushkas.rect.x, lagushkas.rect.y))
        if player.rect.colliderect(lagushkas.rect):
            spike.ahh()
            lagushkas.zanovo()
            player.vitalik += 1
    font = pygame.font.Font(None, 36)
    text = font.render(f"Монеты: {player.vitalik}", True, (255, 30, 203))
    amoznonakulakax.blit(text, (10, 20))

    amoznonakulakax.blit(player.image, (player.rect.x, player.rect.y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()