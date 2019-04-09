import pygame
import time
from math import atan2, sin, cos

pygame.init()

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


screen_width = 1200
screen_height = 600

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Limbo")


bg = pygame.image.load('JailCell1.png')
lvl1 = pygame.image.load('level_1.png')

font = pygame.font.SysFont(None, 100)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [screen_width/2, screen_height/2])


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False

        win.fill(white)
        message_to_screen("Welcome to Rerun",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective of this game is to escape from the prison",
                          black,
                          -30)
        message_to_screen("You need to fight your way through each level without getting caught or shot",
                          black,
                          10)
        message_to_screen("If you get caught or shot, you lose",
                          black,
                          50)
        message_to_screen("Press c to play or q to quit",
                          black,
                          180)
        pygame.display.update()
        clock.tick(15)


# classifying player
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name):
        pygame.sprite.Sprite.__init__(self)
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
        self.image = pygame.image.load('player0.png')

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.lookUp = [pygame.image.load(self.name + '0.png')]
        self.lookDown = [pygame.image.load(self.name + '180.png')]
        self.lookLeft = [pygame.image.load(self.name + '270.png')]
        self.lookRight = [pygame.image.load(self.name + '90.png')]
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


class Player(Character, pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health


player = Player(75, 255, 40, 60, 'player', 6)


class Guard(Character, pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health

    def chase(self):
        global player
        if self.x < player.x:
            self.x += 1
            self.rect.center = (self.x, self.y)
            self.right = True
            self.left = False
            self.up = False
            self.down = False

        elif self.x > player.x:
            self.x -= 1
            self.rect.center = (self.x, self.y)
            self.right = False
            self.left = True
            self.up = False
            self.down = False

        if self.y < player.y:
            self.y += 1
            self.rect.center = (self.x, self.y)
            self.right = False
            self.left = False
            self.up = False
            self.down = True

        elif self.y > player.y:
            self.y -= 1
            self.rect.center = (self.x, self.y)
            self.right = False
            self.left = False
            self.up = True
            self.down = False

        if self.x == player.x and self.y == player.y:
            message_to_screen("You lost", red)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()

        else:
            pass


Guard = Guard(1250, 255, 40, 60, 'Guard', 6)


class Projectile:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):

        pygame.draw.circle(win, self.color, (int(round(self.x, 0)), int(round(self.y, 0))), self.radius)


class Bullet(Projectile):
    def __init__(self, x, y, radius, color, velocity):
        super().__init__(x, y, radius, color)
        self.velocity = velocity
        self.speed = .5


class Click:
    def __init__(self, mouse_pos):
        self.mouse_pos = mouse_pos


b = Bullet(Guard.x, Guard.y, 6, black, 0)
bullets = []
clicks = []
shots = []


# update positions
def prelvlwindow():
    win.blit(bg, (0, 0))
    player.draw()
    Guard.chase()
    Guard.draw()
    lvlup()
    for i in bullets:
        i.draw()
    pygame.display.update()


def lvl1window():
    win.blit(lvl1, (0, 0))
    player.draw()
    lvlup()
    pygame.display.update()


def lvlup():
    if player.x == 1100:
        player.x = 75
        player.y = 255
        player.rect.center = (player.x, player.y)
        player.left = False
        player.right = True
        player.down = False
        player.up = False
        lvl1window()

    else:
        pass


# game loop
clock = pygame.time.Clock()
run = True
playeralive = True


# prelevel code
def prelevel():
    global run
    while run:
        global n

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if keys[pygame.K_r]:
                del shots[:]
                loaded = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(bullets) <= 6:

                    loaded = True
                    if len(shots) == 6:
                        loaded = False

                    def bullet_velocity(change_x, change_y):
                        for bullet in bullets:
                            speed = 25
                            bullet.mouse_position = pygame.mouse.get_pos()
                            bullet.mouse_player_dx = bullet.mouse_position[0] - (player.x + change_x)
                            bullet.mouse_player_dy = bullet.mouse_position[1] - (player.y + change_y)
                            bullet.angle = atan2(bullet.mouse_player_dy, bullet.mouse_player_dx)
                            bullet.new_velocity = (speed * cos(bullet.angle), speed * sin(bullet.angle))

                            n = len(bullets) - 1
                            bullets[n].velocity = bullet.new_velocity

                    mouse_positions = pygame.mouse.get_pos()
                    pos_none = (0, 0)
                    clicks.append(Click(pos_none))

                    if loaded:
                        for click in clicks:
                            s = len(clicks) - 1
                            clicks[s] = mouse_positions

                            if player.left:
                                if clicks[s][0] <= player.x:
                                    bullets.append(Bullet(player.x, player.y + 75, 4, black, 0))
                                    bullet_velocity(0, 75)
                                    shots.append([])
                                    break
                                break

                            if player.right:
                                if clicks[s][0] >= player.x + 42:
                                    bullets.append(Bullet(player.x + 57, player.y + 7, 4, black, 0))
                                    bullet_velocity(57, 7)
                                    shots.append([])
                                    break
                                break

                            if player.up:
                                if clicks[s][1] <= player.y:
                                    bullets.append(Bullet(player.x + 7, player.y, 4, black, 0))
                                    bullet_velocity(7, 0)
                                    shots.append([])
                                    break
                                break

                            if player.down:
                                if clicks[s][1] >= player.y + 42:
                                    bullets.append(Bullet(player.x + 75, player.y + 57, 4, black, 0))
                                    bullet_velocity(75, 57)
                                    shots.append([])
                                    break
                                break

                            if player.lookIdle:
                                if clicks[s][1] <= player.y:
                                    bullets.append(Bullet(player.x + 7, player.y, 4, black, 0))
                                    bullet_velocity(7, 0)
                                    shots.append([])
                                    break
                                break

        for bullet in bullets:
            if screen_width > bullet.x > 0:

                n = 0
                while n <= len(bullets) - 1:
                    bullets[n].x += bullets[n].velocity[0]
                    bullets[n].y += bullets[n].velocity[1]
                    n += 1

                if screen_width < bullet.x or bullet.x < 0:
                    bullets.pop(bullets.index(bullet))

                if screen_height < bullet.y or bullet.y < 0:
                    bullets.pop(bullets.index(bullet))

            else:
                bullets.pop(bullets.index(bullet))

        if keys[pygame.K_a] and player.x > 0 + 3:
            player.x -= player.vel
            player.left = True
            player.right = False
            player.down = False
            player.up = False
            player.rect.center = (player.x, player.y)

        if keys[pygame.K_d] and player.x < screen_width - player.height - 25:
            player.x += player.vel
            player.left = False
            player.right = True
            player.down = False
            player.up = False
            player.rect.center = (player.x, player.y)

        if keys[pygame.K_w] and player.y > 150:
            player.y -= player.vel
            player.left = False
            player.right = False
            player.down = False
            player.up = True
            player.rect.center = (player.x, player.y)

        if keys[pygame.K_s] and player.y < 0 + 365:
            player.y += player.vel
            player.left = False
            player.right = False
            player.down = True
            player.up = False
            player.rect.center = (player.x, player.y)

        prelvlwindow()
        clock.tick(60)


# game starts here
prelevel()


pygame.quit()

