import pygame
pygame.init()


screen = pygame.display.set_mode((640, 700))
screen.fill("blue")
pygame.display.set_caption('SHIP GAME')
fps = 60


running = True
clock = pygame.time.Clock()
plane = pygame.image.load('plane.png')
plane = pygame.transform.scale(plane, (100, 100))
background = pygame.image.load('background.jpeg')
background = pygame.transform.scale(background, (640, 700))
bullet = pygame.image.load('bullet.jpg')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(plane, (0, 0))
    
    pygame.display.flip()

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('plane.png')
        self.rect = self.image.get_rect()
        self.rect.center = (640 // 2, 650)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 700:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bullet.jpg')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()