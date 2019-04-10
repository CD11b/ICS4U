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

bg = pygame.image.load('JailCell1.png')

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

        self.hitbox = (self.x + 20, self.y, 100, 80)

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

        self.hitbox = (self.x - 8, self.y, 90, 90)

        #pygame.draw.rect(win, (255,0,0), self.hitbox,2) :this was to draw a hitbox around the character so I could edit the dimensions. 
        


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

class GuardGun:
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


        #adding hitbox, and health to the guard 
        self.hitbox = (self.x + 20, self.y, 100, 68)
        self.health = 10
        self.visible = True



    def draw(self):
        #only load the guard image if the guard it alive
        if self.visible:
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

            self.hitbox = (self.x - 10, self.y, 90, 80)

            #HEALTHBAR
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 -self.health)), 10))


            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        #defining how the guards health interacts with the image and healthbar level
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
    
        print('hit')


def GuardGunLeft():
    if keys[pygame.K_LEFT] and player.x > 0 + 3:
        if not player.left and player.right and player.up and player.down:
            GuardGun.x -= GuardGun.vel
            GuardGun.left = True
            GuardGun.right = False
            GuardGun.down = False
            GuardGun.up = False
        else:
            pass


def GuardGunRight():
    if keys[pygame.K_RIGHT] and player.x < screen_width - player.height - 25:
        if not player.left and player.right and player.up and player.down:
            GuardGun.x -= Guard.vel
            GuardGun.left = False
            GuardGun.right = True
            GuardGun.down = False
            GuardGun.up = False
        else:
            pass


def GuardGunUp():
    if keys[pygame.K_UP] and player.y > 0:
        if not player.left and player.right and player.up and player.down:
            GuardGun.y += GuardGun.vel
            GuardGun.left = False
            GuardGun.right = False
            GuardGun.down = False
            GuardGun.up = True
        else:
            pass


def GuardGunDown():
    if keys[pygame.K_DOWN] and player.y < 0 + 365:
        if not player.left and player.right and player.up and player.down:
            GuardGun.y -= GuardGun.vel
            GuardGun.left = False
            GuardGun.right = False
            GuardGun.down = True
            GuardGun.up = False
        else:
            pass


GuardGun = GuardGun(200, 200, 40, 60, 'GuardGun')



player = Player(100, 100, 40, 60, 'player')

clock = pygame.time.Clock()
run = True

b = Bullet(player.x, player.y, 6, black, 0)


bullets = []


def redrawGameWindow():
    win.blit(bg, (0, 0))
    player.draw()
    GuardGun.draw()
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
                bullets.append(Bullet(player.x, player.y, 6, black, 0))

                for bullet in bullets:

                    speed = 25
                    bullet.mouse_position = pygame.mouse.get_pos()
                    bullet.mouse_player_dx = bullet.mouse_position[0] - player.x
                    bullet.mouse_player_dy = bullet.mouse_position[1] - player.y
                    bullet.angle = atan2(bullet.mouse_player_dy, bullet.mouse_player_dx)
                    bullet.new_velocity = (speed * cos(bullet.angle), speed * sin(bullet.angle))

                    n = len(bullets) - 1
                    bullets[n].velocity = bullet.new_velocity


    for bullet in bullets:

        if bullet.y - bullet.radius < GuardGun.hitbox[1] + GuardGun.hitbox[3] and bullet.y + bullet.radius > GuardGun.hitbox[1]:
            if bullet.x + bullet.radius > GuardGun.hitbox[0] and bullet.x - bullet.radius < GuardGun.hitbox[0] + GuardGun.hitbox[2]:
                GuardGun.hit()
                bullets.pop(bullets.index(bullet))

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



    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player.speed
        player.left = True
        player.right = False
        player.down = False
        player.up = False
        GuardGun.x -= GuardGun.vel
        GuardGun.left = True
        GuardGun.right = False
        GuardGun.down = False
        GuardGun.up = False
        GuardGunLeft()

    if keys[pygame.K_RIGHT] and player.x + player.width < screen_width - player.width:
        player.x += player.speed
        player.left = False
        player.right = True
        player.down = False
        player.up = False
        GuardGun.x += GuardGun.vel
        GuardGun.left = False
        GuardGun.right = True
        GuardGun.down = False
        GuardGun.up = False
        GuardGunRight()


    if keys[pygame.K_UP] and player.y > 0:
        player.y -= player.speed
        player.left = False
        player.right = False
        player.down = False
        player.up = True
        GuardGun.y -= GuardGun.vel
        GuardGun.left = False
        GuardGun.right = False
        GuardGun.down = False
        GuardGun.up = True
        GuardGunUp()



    if keys[pygame.K_DOWN] and player.y + player.width < screen_height - player.height:
        player.y += player.speed
        player.left = False
        player.right = False
        player.down = True
        player.up = False
        GuardGun.y += GuardGun.vel
        GuardGun.left = False
        GuardGun.right = False
        GuardGun.down = True
        GuardGun.up = False
        GuardGunDown()


    redrawGameWindow()
    clock.tick(120)

pygame.quit()
