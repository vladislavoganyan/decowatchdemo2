import random

import pygame

pygame.init()
nachalo = True
konec = False
FPS = 60
clock = pygame.time.Clock()
dlina = 800
shirina = 500
pepe_gap = 180
ochko_valeri = 0
pass_pepe = False
pepe_frequence = random.randint(2000, 2000)
storona_pepe = pygame.time.get_ticks() - pepe_frequence

background = pygame.transform.scale(pygame.image.load("zelti.jpg"), (dlina, shirina))
zemla = pygame.transform.scale(pygame.image.load("zemla.png"), (900, 100))
proigral = pygame.transform.scale(pygame.image.load("Безымянный.png"), (dlina, shirina))
amoznonakulakax = pygame.display.set_mode((dlina, shirina))

scroll_speed = 3
ground_scroll = 0


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []

        for num in range(1, 13):
            try:
                img = pygame.image.load(f"птица хуйня/{num}.png")
                self.images.append(img)
            except:
                self.images.append(pygame.Surface((50, 50)))

        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 0
        self.click = False

    def update(self):
        self.velocity += 0.4
        if self.rect.bottom < 450 and self.rect.bottom > 0:
            self.rect.y += self.velocity
        else:
            amoznonakulakax.blit(proigral, (0, 0))
        self.counter += 1
        flap_cooldown = 5

        if self.counter >= flap_cooldown:
            self.counter = 0
            self.index = (self.index + 1) % len(self.images)

        self.image = self.images[self.index]
        self.image = pygame.transform.rotate(self.images[self.index], self.velocity * 3)
        self.image = pygame.transform.flip(self.image, True, False)


        if pygame.mouse.get_pressed()[0] == 1 and not self.click:
            self.click = True
            self.velocity = -6
        if pygame.mouse.get_pressed()[0]==0:
            self.click = False

class Pepe(pygame.sprite.Sprite):
    def __init__(self, x, y, vakuol):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("strogo.png")
        self.image = pygame.transform.scale(self.image, (70, 200))
        self.rect = self.image.get_rect(topleft=(x, y))
        if vakuol == "top":
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(bottomleft = (x, y-pepe_gap//2))
        elif vakuol == "bottom":
            self.rect = self.image.get_rect(topleft = (x, y+pepe_gap//2))
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()


def show_text(label, x, y):
    f1 = pygame.font.Font(None, 36)
    text = f1.render(label, True, (180, 0, 0))
    amoznonakulakax.blit(text,(x, y))



bird = Bird(35,  50)
bird_group = pygame.sprite.Group()
bird_group.add(bird)
pepe_grupovuha_s_Valeroi_i_Vanei = pygame.sprite.Group()

run = True
while run:
    clock.tick(FPS)

    time_now = pygame.time.get_ticks()
    if time_now - storona_pepe > pepe_frequence:
        pepe_height = random.randint(-100, 100)
        bottom_pepe = Pepe(300, shirina // 2 + pepe_height, "bottom")
        top_pepe = Pepe(300, shirina // 2 + pepe_height, "top")
        pepe_grupovuha_s_Valeroi_i_Vanei.add(bottom_pepe)
        pepe_grupovuha_s_Valeroi_i_Vanei.add(top_pepe)
        storona_pepe = time_now
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    if pygame.sprite.groupcollide(bird_group, pepe_grupovuha_s_Valeroi_i_Vanei, False, False):
        run = False

    if len(pepe_grupovuha_s_Valeroi_i_Vanei) > 0:
        if bird_group.sprites()[0].rect.left > pepe_grupovuha_s_Valeroi_i_Vanei.sprites()[0].rect.left:
            if bird_group.sprites()[0].rect.right > pepe_grupovuha_s_Valeroi_i_Vanei.sprites()[0].rect.right:
                if pass_pepe == False:
                    pass_pepe = True
        if pass_pepe == True:
            if bird_group.sprites()[0].rect.left > pepe_grupovuha_s_Valeroi_i_Vanei.sprites()[0].rect.right:
                ochko_valeri += 1
                pass_pepe = False
    amoznonakulakax.blit(background, (0, 0))

    amoznonakulakax.blit(zemla, (ground_scroll, 400))
    amoznonakulakax.blit(zemla, (ground_scroll + 900, 400))


    amoznonakulakax.blit(bird.image, bird.rect)

    pepe_grupovuha_s_Valeroi_i_Vanei.draw(amoznonakulakax)

    ground_scroll -= scroll_speed

    if ground_scroll <= -900:
        ground_scroll = 0
    pepe_grupovuha_s_Valeroi_i_Vanei.update()
    bird.update()
    show_text("kol-vo ochkov:%s" %ochko_valeri, 100, 100)
    pygame.display.flip()


    #if nachalo == True:
    #    pygame.time.wait(2000)
    #    nachalo = False

pygame.quit()