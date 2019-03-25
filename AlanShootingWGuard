import pygame
from math import atan2, degrees, pi, sin, cos, tan


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
        self.speed = 20
        self.left = False
        self.right = False
        self.down = False
        self.up = False

        self.lookUp = [pygame.image.load(self.name + '0.png')]
        self.lookDown = [pygame.image.load(self.name + '180.png')]
        self.lookLeft = [pygame.image.load(self.name + '270.png')]
        self.lookRight = [pygame.image.load(self.name + '90.png')]
        self.lookIdle = [pygame.image.load(self.name + '0.png')]

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


class Projectile:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 10


    def draw(self):
        pygame.draw.circle(win, self.color, (int(round(self.x, 0)), int(round(self.y, 0))), self.radius)


class Bullet(Projectile):
    def __init__(self, x, y, radius, color, velocity):
        super().__init__(x, y, radius, color)
        self.velocity = velocity

class GuardFull:
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

        self.lookUp = [pygame.image.load(self.name + '0.png')]
        self.lookDown = [pygame.image.load(self.name + '180.png')]
        self.lookLeft = [pygame.image.load(self.name + '270.png')]
        self.lookRight = [pygame.image.load(self.name + '90.png')]
        self.lookIdle = [pygame.image.load(self.name + '180.png')]

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


def GuardFullLeft():
    if keys[pygame.K_LEFT] and prinser.x > 0 + 3:
        if not prinser.left and prinser.right and prinser.up and prinser.down:
            GuardFull.x -= GuardFull.vel
            GuardFull.left = True
            GuardFull.right = False
            GuardFull.down = False
            GuardFull.up = False
        else:
            pass


def GuardFullRight():
    if keys[pygame.K_RIGHT] and prinser.x < screen_width - prinser.height - 25:
        if not prinser.left and prinser.right and prinser.up and prinser.down:
            GuardFull.x -= Guard.vel
            GuardFull.left = False
            GuardFull.right = True
            GuardFull.down = False
            GuardFull.up = False
        else:
            pass


def GuardFullUp():
    if keys[pygame.K_UP] and prinser.y > 0:
        if not prinser.left and prinser.right and prinser.up and prinser.down:
            GuardFull.y += GuardFull.vel
            GuardFull.left = False
            GuardFull.right = False
            GuardFull.down = False
            GuardFull.up = True
        else:
            pass


def GuardFullDown():
    if keys[pygame.K_DOWN] and prinser.y < 0 + 365:
        if not prinser.left and prinser.right and prinser.up and prinser.down:
            GuardFull.y -= GuardFull.vel
            GuardFull.left = False
            GuardFull.right = False
            GuardFull.down = True
            GuardFull.up = False
        else:
            pass


GuardFull = GuardFull(200, 200, 40, 60, 'GuardFull')



prinser = Player(100, 100, 40, 60, 'prinser')

clock = pygame.time.Clock()
run = True

b = Bullet(prinser.x, prinser.y, 6, black, 0)


bullets = []


def redrawGameWindow():
    win.blit(bg, (0, 0))
    prinser.draw()
    GuardFull.draw()
    for bullet in bullets:
        bullet.draw()
    pygame.display.update()



while run:
    global n

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(bullets) < 6:
                bullets.append(Bullet(prinser.x, prinser.y, 6, black, 0))

                for bullet in bullets:

                    speed = 10
                    bullet.mouse_position = pygame.mouse.get_pos()
                    bullet.mouse_player_dx = bullet.mouse_position[0] - prinser.x
                    bullet.mouse_player_dy = bullet.mouse_position[1] - prinser.y
                    bullet.angle = atan2(bullet.mouse_player_dy, bullet.mouse_player_dx)
                    bullet.new_velocity = (speed * cos(bullet.angle), speed * sin(bullet.angle))

                    n = len(bullets) - 1
                    bullets[n].velocity = bullet.new_velocity


    for bullet in bullets:
        if screen_width > bullet.x > 0:

            n = 0
            while n <= len(bullets) - 1:
                bullets[n].x += bullets[n].velocity[0]
                bullets[n].y += bullets[n].velocity[1]
                n += 1

            if screen_width < bullet.x < 0:
                bullets.pop(bullets.index(bullet))

            if screen_height < bullet.y > 0:
                bullets.pop(bullets.index(bullet))

        else:
            bullets.pop(bullets.index(bullet))



    if keys[pygame.K_LEFT] and prinser.x > 0:
        prinser.x -= prinser.speed
        prinser.left = True
        prinser.right = False
        prinser.down = False
        prinser.up = False
        GuardFull.x -= GuardFull.vel
        GuardFull.left = True
        GuardFull.right = False
        GuardFull.down = False
        GuardFull.up = False
        GuardFullLeft()

    if keys[pygame.K_RIGHT] and prinser.x + prinser.width < screen_width - prinser.width:
        prinser.x += prinser.speed
        prinser.left = False
        prinser.right = True
        prinser.down = False
        prinser.up = False
        GuardFull.x += GuardFull.vel
        GuardFull.left = False
        GuardFull.right = True
        GuardFull.down = False
        GuardFull.up = False
        GuardFullRight()


    if keys[pygame.K_UP] and prinser.y > 0:
        prinser.y -= prinser.speed
        prinser.left = False
        prinser.right = False
        prinser.down = False
        prinser.up = True
        GuardFull.y -= GuardFull.vel
        GuardFull.left = False
        GuardFull.right = False
        GuardFull.down = False
        GuardFull.up = True
        GuardFullUp()



    if keys[pygame.K_DOWN] and prinser.y + prinser.width < screen_height - prinser.height:
        prinser.y += prinser.speed
        prinser.left = False
        prinser.right = False
        prinser.down = True
        prinser.up = False
        GuardFull.y += GuardFull.vel
        GuardFull.left = False
        GuardFull.right = False
        GuardFull.down = True
        GuardFull.up = False
        GuardFullDown()


    redrawGameWindow()
    clock.tick(120)

pygame.quit()
