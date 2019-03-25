import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

screen_width = 1200
screen_height = 600

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Limbo")


bg = pygame.image.load('JailCell1.jpg')


class Player:
    def __init__(self, x, y, width, height, name):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.down = False
        self.up = False
        self.image = pygame.image.load('player0.jpg')

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.lookUp = [pygame.image.load(self.name + '0.jpg')]
        self.lookDown = [pygame.image.load(self.name + '180.jpg')]
        self.lookLeft = [pygame.image.load(self.name + '270.jpg')]
        self.lookRight = [pygame.image.load(self.name + '90.jpg')]
        self.lookIdle = [pygame.image.load(self.name + '0.jpg')]

    def draw(self):
        if self.left:
            win.blit(self.lookLeft[0], (self.x, self.y))

        elif self.right:
            win.blit(self.lookRight[0], (self.x, self.y))

        elif self.down:
            win.blit(self.lookDown[0], (self.x, self.y))

        elif self.up:
            win.blit(self.lookUp[0], (self.x, self.y))

        else:
            win.blit(self.lookIdle[0], (self.x, self.y))


player = Player(125, 50, 40, 60, 'player')


class Guard:
    def __init__(self, x, y, width, height, name):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.left = False
        self.right = False
        self.down = False
        self.up = False
        self.image = pygame.image.load('Guard0.jpg')

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.lookUp = [pygame.image.load(self.name + '0.jpg')]
        self.lookDown = [pygame.image.load(self.name + '180.jpg')]
        self.lookLeft = [pygame.image.load(self.name + '270.jpg')]
        self.lookRight = [pygame.image.load(self.name + '90.jpg')]
        self.lookIdle = [pygame.image.load(self.name + '180.jpg')]

    def draw(self):
        if self.left:
            win.blit(self.lookLeft[0], (self.x, self.y))

        elif self.right:
            win.blit(self.lookRight[0], (self.x, self.y))

        elif self.down:
            win.blit(self.lookDown[0], (self.x, self.y))

        elif self.up:
            win.blit(self.lookUp[0], (self.x, self.y))

        else:
            win.blit(self.lookIdle[0], (self.x, self.y))

    def update(self):
        global player
        if self.x < player.x:
            self.x += 1
            self.rect.center = (self.x, self.y)

        elif self.x > player.x:
            self.x -= 1
            self.rect.center = (self.x, self.y)

        if self.y < player.y:
            self.y += 1
            self.rect.center = (self.x, self.y)

        elif self.y > player.y:
            self.y -= 1
            self.rect.center = (self.x, self.y)


Guard = Guard(200, 200, 40, 60, 'Guard')


clock = pygame.time.Clock()
run = True


def redrawGameWindow():
    win.blit(bg, (0, 0))
    player.draw()
    Guard.draw()
    pygame.display.update()


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > 0 + 3:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.down = False
        player.up = False
        player.rect.center = (player.x, player.y)

    if keys[pygame.K_RIGHT] and player.x < screen_width - player.height - 25:
        player.x += player.vel
        player.left = False
        player.right = True
        player.down = False
        player.up = False
        player.rect.center = (player.x, player.y)

    if keys[pygame.K_UP] and player.y > 0:
        player.y -= player.vel
        player.left = False
        player.right = False
        player.down = False
        player.up = True
        player.rect.center = (player.x, player.y)

    if keys[pygame.K_DOWN] and player.y < 0 + 365:
        player.y += player.vel
        player.left = False
        player.right = False
        player.down = True
        player.up = False
        player.rect.center = (player.x, player.y)

    redrawGameWindow()
    Guard.update()
    clock.tick(60)

pygame.quit()
