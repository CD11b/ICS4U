import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

screen_width = 500
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Limbo")


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

        self.lookUp = [pygame.image.load(self.name + '90.png')]
        self.lookDown = [pygame.image.load(self.name + '270.png')]
        self.lookLeft = [pygame.image.load(self.name + '180.png')]
        self.lookRight = [pygame.image.load(self.name + '0.png')]
        self.lookIdle = [pygame.image.load(self.name + '90.png')]

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


guard = Player(50, 50, 40, 60, 'guard')

clock = pygame.time.Clock()
run = True


def redrawGameWindow():
    win.fill(black)
    guard.draw()
    pygame.display.update()


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and guard.x > 0:
        guard.x -= guard.vel
        guard.left = True
        guard.right = False
        guard.down = False
        guard.up = False

    if keys[pygame.K_RIGHT] and guard.x < screen_width - guard.width:
        guard.x += guard.vel
        guard.left = False
        guard.right = True
        guard.down = False
        guard.up = False

    if keys[pygame.K_UP] and guard.y > 0:
        guard.y -= guard.vel
        guard.left = False
        guard.right = False
        guard.down = False
        guard.up = True

    if keys[pygame.K_DOWN] and guard.y < screen_height - guard.height:
        guard.y += guard.vel
        guard.left = False
        guard.right = False
        guard.down = True
        guard.up = False

    redrawGameWindow()
    clock.tick(60)

pygame.quit()
