import pygame
from math import atan2, sin, cos

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


screen_width = 1200
screen_height = 600

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Limbo")


bg = pygame.image.load('JailCell1.png')
lvl1 = pygame.image.load('lvl1.png')

font = pygame.font.SysFont(None, 100)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    win.blit(screen_text, [screen_width/2, screen_height/2])


# classifying player
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.left = False
        self.right = False
        self.down = False
        self.up = False

        self.lookUp = pygame.image.load(self.name + '90.png')
        self.lookDown = pygame.image.load(self.name + '270.png')
        self.lookLeft = pygame.image.load(self.name + '180.png')
        self.lookRight = pygame.image.load(self.name + '0.png')
        self.lookIdle = pygame.image.load(self.name + '0.png')

        self.rect = self.lookIdle.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self):
        if self.left:
            win.blit(self.lookLeft, (self.x, self.y))
            self.hitbox = (self.x, self.y, self.height, self.width)
            pygame.draw.rect(win, red, self.hitbox, 2)

        elif self.right:
            win.blit(self.lookRight, (self.x, self.y))
            self.hitbox = (self.x, self.y, self.height, self.width)
            pygame.draw.rect(win, red, self.hitbox, 2)

        elif self.down:
            win.blit(self.lookDown, (self.x, self.y))
            self.hitbox = (self.x, self.y, self.width, self.height)
            pygame.draw.rect(win, red, self.hitbox, 2)

        elif self.up:
            win.blit(self.lookUp, (self.x, self.y))
            self.hitbox = (self.x, self.y, self.width, self.height)
            pygame.draw.rect(win, red, self.hitbox, 2)

        else:
            win.blit(self.lookIdle, (self.x, self.y))



class Player(Character, pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health
        self.speed = 5


class Mob(Character, pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health
        self.speed = .5

    def chase(self):

        if self.x < player.x:
            self.x += self.speed

            self.right = True
            self.left = False
            self.up = False
            self.down = False

        if self.x > player.x:
            self.x -= self.speed

            self.right = False
            self.left = True
            self.up = False
            self.down = False

        if self.y < player.y:
            self.y += self.speed

            self.right = False
            self.left = False
            self.up = False
            self.down = True

        if self.y > player.y:
            self.y -= self.speed

            self.right = False
            self.left = False
            self.up = True
            self.down = False

        if self.x == player.x and self.y == player.y:
            message_to_screen("You lost", red)
            pygame.display.update()
            pygame.quit()

        else:
            pass


class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):

        pygame.draw.circle(win, self.color, (int(round(self.x, 0)), int(round(self.y, 0))), self.radius)


class Bullet(Projectile):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.velocity = 0
        self.radius = 2
        self.color = black
        self.speed = 5


class Click:
    def __init__(self, mouse_pos):
        self.mouse_pos = mouse_pos


guard = Mob(1250, 255, 82, 61, 'GuardGun', 6)
player = Player(200, 200, 82, 49, 'prisoner', 6)
b = Bullet(player.x, player.y)
bullets = []
clicks = []
shots = []

def redraw():
    win.blit(bg, (0, 0))
    player.draw()
    guard.chase()
    guard.draw()
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

        player.left = False
        player.right = True
        player.down = False
        player.up = False
        lvl1window()

    else:
        pass


clock = pygame.time.Clock()
run = True

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
            if len(bullets) < 6:

                loaded = True
                if len(shots) == 6:
                    loaded = False

                def bullet_velocity(change_x, change_y):
                    for bullet in bullets:

                        n = len(bullets) - 1

                        bullet.mouse_position = pygame.mouse.get_pos()
                        bullet.mouse_player_dx = bullet.mouse_position[0] - (player.x + change_x)
                        bullet.mouse_player_dy = bullet.mouse_position[1] - (player.y + change_y)
                        bullet.angle = atan2(bullet.mouse_player_dy, bullet.mouse_player_dx)
                        bullet.new_velocity = (bullets[n].speed * cos(bullet.angle), bullets[n].speed * sin(bullet.angle))
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
                                bullets.append(Bullet(player.x, player.y + 75))
                                bullet_velocity(0, 75)
                                shots.append([])
                                break
                            break

                        if player.right:
                            if clicks[s][0] >= player.x + 200:
                                if clicks[s][1] >= player.y - 200:
                                    if clicks[s][1] <= player.y + 200:
                                        bullets.append(Bullet(player.x + 57, player.y + 7))
                                        bullet_velocity(57, 7)
                                        shots.append([])
                                        break
                            break

                        if player.up:
                            if clicks[s][1] <= player.y - 100:
                                if clicks[s][1] <= player.x + 400:
                                    bullets.append(Bullet(player.x + 7, player.y))
                                    bullet_velocity(7, 0)
                                    shots.append([])
                                    break
                            break

                        if player.down:
                            if clicks[s][1] >= player.y + 42:
                                bullets.append(Bullet(player.x + 75, player.y + 57))
                                bullet_velocity(75, 57)
                                shots.append([])
                                break
                            break

                        if player.lookIdle:
                            if clicks[s][1] <= player.y:
                                bullets.append(Bullet(player.x + 7, player.y))
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
                try:
                    bullets.pop(bullets.index(bullet))

                except ValueError:
                    pass

        else:
            bullets.pop(bullets.index(bullet))

    if keys[pygame.K_a] and player.x > 0:
        player.x -= player.speed
        player.left = True
        player.right = False
        player.down = False
        player.up = False

    if keys[pygame.K_d] and player.x + player.width < screen_width - player.width:
        player.x += player.speed
        player.left = False
        player.right = True
        player.down = False
        player.up = False

    if keys[pygame.K_w] and player.y > 0:
        player.y -= player.speed
        player.left = False
        player.right = False
        player.down = False
        player.up = True

    if keys[pygame.K_s] and player.y + player.width < screen_height - player.height:
        player.y += player.speed
        player.left = False
        player.right = False
        player.down = True
        player.up = False

    redraw()
    clock.tick(60)

pygame.quit()
