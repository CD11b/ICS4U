import pygame
from math import atan2, sin, cos

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

screen_width = 1200
screen_height = 600

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Limbo")


class Character:
    def __init__(self, x, y, width, height, name):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
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


class Mob(Character):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health


class Player(Character):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health


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


clock = pygame.time.Clock()
run = True

guard = Mob(100, 100, 82, 49, 'GuardGun', 6)
player = Player(200, 200, 40, 60, 'prisoner', 6)
b = Bullet(guard.x, guard.y, 6, black, 0)
bullets = []
clicks = []
shots = []

def redrawGameWindow():
    win.fill(green)
    guard.draw()
    # player.draw()
    for i in bullets:
        i.draw()
    pygame.display.update()


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
                        speed = 25
                        bullet.mouse_position = pygame.mouse.get_pos()
                        bullet.mouse_player_dx = bullet.mouse_position[0] - (guard.x + change_x)
                        bullet.mouse_player_dy = bullet.mouse_position[1] - (guard.y + change_y)
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

                        if guard.left:
                            if clicks[s][0] <= guard.x:
                                bullets.append(Bullet(guard.x, guard.y + 75, 4, black, 0))
                                bullet_velocity(0, 75)
                                shots.append([])
                                break
                            break

                        if guard.right:
                            if clicks[s][0] >= guard.x + 42:
                                bullets.append(Bullet(guard.x + 57, guard.y + 7, 4, black, 0))
                                bullet_velocity(57, 7)
                                shots.append([])
                                break
                            break

                        if guard.up:
                            if clicks[s][1] <= guard.y:
                                bullets.append(Bullet(guard.x + 7, guard.y, 4, black, 0))
                                bullet_velocity(7, 0)
                                shots.append([])
                                break
                            break

                        if guard.down:
                            if clicks[s][1] >= guard.y + 42:
                                bullets.append(Bullet(guard.x + 75, guard.y + 57, 4, black, 0))
                                bullet_velocity(75, 57)
                                shots.append([])
                                break
                            break

                        if guard.lookIdle:
                            if clicks[s][1] <= guard.y:
                                bullets.append(Bullet(guard.x + 7, guard.y, 4, black, 0))
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

    if keys[pygame.K_a] and guard.x > 0:
        guard.x -= guard.speed
        guard.left = True
        guard.right = False
        guard.down = False
        guard.up = False

    if keys[pygame.K_d] and guard.x + guard.width < screen_width - guard.width:
        guard.x += guard.speed
        guard.left = False
        guard.right = True
        guard.down = False
        guard.up = False

    if keys[pygame.K_w] and guard.y > 0:
        guard.y -= guard.speed
        guard.left = False
        guard.right = False
        guard.down = False
        guard.up = True

    if keys[pygame.K_s] and guard.y + guard.width < screen_height - guard.height:
        guard.y += guard.speed
        guard.left = False
        guard.right = False
        guard.down = True
        guard.up = False

    redrawGameWindow()
    clock.tick(60)

pygame.quit()
