import pygame
import time
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


def text_objects(text, color, size):
    if size == "small":
        textsurface = smallfont.render(text, True, color)
    elif size == "medium":
        textsurface = medfont.render(text, True, color)
    elif size == "large":
        textsurface = largefont.render(text, True, color)

    return textsurface, textsurface.get_rect()


def message_to_screen(msg, color, x, y, size):
    textsurf, textrect = text_objects(msg, color, size)
    textrect.center = (x, y)
    win.blit(textsurf, textrect)


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
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        win.fill(black)
        message_to_screen("Welcome to Rerun", green, (screen_width / 2), (screen_height / 2) - 100, "small")
        message_to_screen("The objective of this game is to escape from the prison", white, (screen_width / 2),
                          (screen_height / 2) - 30, "small")
        message_to_screen("You need to fight your way through each level without getting caught or shot", white,
                          (screen_width / 2), (screen_height / 2) + 10, "small")
        message_to_screen("If you get caught or shot, you lose", white, (screen_width / 2), (screen_height / 2) + 50,
                          "small")
        message_to_screen("Press c to continue or q to quit", red, (screen_width / 2), (screen_height / 2) + 180,
                          "small")
        pygame.display.update()


def how_to():
    howto = True
    while howto:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    howto = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        win.fill(black)
        message_to_screen("Instructions", green, (screen_width / 2), (screen_height / 2) - 150, "large")
        message_to_screen("Press W to move up, A to move left, S to move down, and D to move right", white,
                          (screen_width / 2), (screen_height / 2) - 30, "small")
        message_to_screen("Using the mouse to shoot, and press R to recoil", white, (screen_width / 2),
                          (screen_height / 2) + 10, "small")
        message_to_screen("GLHF!", white, (screen_width / 2), (screen_height / 2) + 50, "small")
        message_to_screen("Press p to play or q to quit", red, (screen_width / 2), (screen_height / 2) + 180, "small")
        pygame.display.update()


player_bullets = []
guard_bullets = []
guards = []
clicks = []
shots = []
stop = []


class Click:
    def __init__(self, mouse_pos):
        self.mouse_pos = mouse_pos


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

        self.hitbox = (self.x - 10, self.y, 90, 80)

        # HEALTHBAR
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

    def shot(self):
        if self.health > 0:
            self.health -= 1
        else:
            pass


class Player(Character, pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = 10
        self.speed = 5
        self.loaded = True
        self.alive = True

    def bullet_velocity(self, change_x, change_y):
        for bullet in player_bullets:
            n = len(player_bullets) - 1

            bullet.mouse_position = pygame.mouse.get_pos()
            bullet.mouse_player_dx = bullet.mouse_position[0] - (self.x + change_x)
            bullet.mouse_player_dy = bullet.mouse_position[1] - (self.y + change_y)
            bullet.angle = atan2(bullet.mouse_player_dy, bullet.mouse_player_dx)
            bullet.new_velocity = (
            player_bullets[n].speed * cos(bullet.angle), player_bullets[n].speed * sin(bullet.angle))
            player_bullets[n].velocity = bullet.new_velocity

    def bulletVelCalc(self):
        mouse_positions = pygame.mouse.get_pos()
        pos_none = (0, 0)
        clicks.append(Click(pos_none))

        for click in clicks:
            s = len(clicks) - 1
            clicks[s] = mouse_positions
            if self.loaded == True:

                if self.left:

                    if clicks[s][0] <= (self.x + self.height / 2 + self.width / 2) - 100:
                        if clicks[s][1] <= (self.y + self.height / 2 + self.width / 2) + 200:
                            if clicks[s][1] >= (self.y + self.height / 2 + self.width / 2) - 200:
                                player_bullets.append(Bullet(self.x, self.y + 75))
                                self.bullet_velocity(0, 75)
                                shots.append([])
                                break
                    break

                if self.right:

                    if clicks[s][0] >= (self.x + self.height / 2 + self.width / 2) + 100:
                        if clicks[s][1] >= (self.y + self.height / 2 + self.width / 2) - 200:
                            if clicks[s][1] <= (self.y + self.height / 2 + self.width / 2) + 200:
                                player_bullets.append(Bullet(self.x + 57, self.y + 7))
                                self.bullet_velocity(57, 7)
                                shots.append([])
                                break
                    break

                if self.up:
                    if clicks[s][1] <= (self.y + self.height / 2 + self.width / 2) - 100:
                        if clicks[s][0] >= (self.x + self.height / 2 + self.width / 2) - 200:
                            if clicks[s][0] <= (self.x + self.height / 2 + self.width / 2) + 200:
                                player_bullets.append(Bullet(self.x + 7, self.y))
                                self.bullet_velocity(7, 0)
                                shots.append([])
                                break
                    break

                if self.down:
                    if clicks[s][1] >= self.y + 200:
                        if clicks[s][0] >= (self.x + self.height / 2 + self.width / 2) - 200:
                            if clicks[s][0] <= (self.x + self.height / 2 + self.width / 2) + 200:
                                player_bullets.append(Bullet(self.x + 75, self.y + 57))
                                self.bullet_velocity(75, 57)
                                shots.append([])
                                break
                    break

                if clicks[s][0] >= (self.x + self.height / 2 + self.width / 2) + 100:
                    if clicks[s][1] >= (self.y + self.height / 2 + self.width / 2) - 200:
                        if clicks[s][1] <= (self.y + self.height / 2 + self.width / 2) + 200:
                            player_bullets.append(Bullet(self.x + 57, self.y + 7))
                            self.bullet_velocity(57, 7)
                            shots.append([])
                            break
                break

        else:
            pass


guard_shots = []
guards_killed = []


class Mob(Character, pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health
        self.speed = .5
        self.hitbox = (self.x - 8, self.y, 90, 90)
        self.last = pygame.time.get_ticks()
        self.shooting_cooldown = 200
        self.loading_cooldown = 200

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
            message_to_screen("You lost", red, player.x, player.y, size="medium")
            pygame.display.update()
            time.sleep(3)
            pygame.quit()

        else:
            pass

        self.hitbox = (self.x - 10, self.y, 90, 80)

        # HEALTHBAR
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

    def bullet_velocity(self, change_x, change_y):
        for bullet in guard_bullets:
            n = len(guard_bullets) - 1

            bullet.guard_player_dx = (player.x - player.width) / 2 - (self.x - self.width) / 2
            bullet.guard_player_dy = (player.y - player.height) / 2 - (self.y - self.height) / 2
            bullet.angle = atan2(bullet.guard_player_dy, bullet.guard_player_dx)
            bullet.new_velocity = (
            guard_bullets[n].speed * cos(bullet.angle), guard_bullets[n].speed * sin(bullet.angle))
            guard_bullets[n].velocity = bullet.new_velocity

    def shoot(self):

        if len(guard_shots) <= 8:
            now = pygame.time.get_ticks()
            if now - self.last >= 1500:
                self.last = now
                self.start_shoot()

        if len(guard_shots) > 8:

            now = pygame.time.get_ticks()
            if now - self.last >= 4000:
                self.last = now
                del guard_shots[:]

    def start_shoot(self):

        if self.left:
            guard_bullets.append(Bullet(self.x, self.y + 75))
            self.bullet_velocity(0, 75)
            guard_shots.append([])

        if self.right:
            guard_bullets.append(Bullet(self.x + 57, self.y + 7))
            self.bullet_velocity(57, 7)
            guard_shots.append([])

        if self.up:
            guard_bullets.append(Bullet(self.x + 7, self.y))
            self.bullet_velocity(7, 0)
            guard_shots.append([])

        if self.down:

            guard_bullets.append(Bullet(self.x + 75, self.y + 57))
            self.bullet_velocity(75, 57)
            guard_shots.append([])

        else:
            pass

    def bullet_change(self):

        for bullet in guard_bullets:

            if bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > \
                    player.hitbox[1]:
                if bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox[0] + \
                        player.hitbox[2]:
                    player.shot()

                    if player.health == 0:
                        pass
                        message_to_screen("You lost", red, player.x, player.y, size="medium")
                        pygame.display.update()
                        pygame.quit()

                    guard_bullets.pop(guard_bullets.index(bullet))

            if screen_width > bullet.x > 0:

                n = 0
                while n <= len(guard_bullets) - 1:
                    guard_bullets[n].x += guard_bullets[n].velocity[0]
                    guard_bullets[n].y += guard_bullets[n].velocity[1]
                    n += 1

                if screen_width < bullet.x or bullet.x < 0:
                    guard_bullets.pop(guard_bullets.index(bullet))

                if screen_height < bullet.y or bullet.y < 0:
                    try:
                        guard_bullets.pop(guard_bullets.index(bullet))

                    except ValueError:
                        pass

            else:
                try:
                    guard_bullets.pop(guard_bullets.index(bullet))

                except ValueError:
                    pass

guardTowerBullets = []
guardTowerShots = []
guardTowers = []
guardTowersKilled = []

class GuardTower(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, health):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.hitbox = (self.x - 10, self.y, self.width, self.height)

        pygame.draw.rect(win, red, self.hitbox, 2)
        self.last = pygame.time.get_ticks()
        self.shooting_cooldown = 200
        self.loading_cooldown = 200

    def draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

    def shot(self):
        if self.health > 0:
            self.health -= 1
        else:
            pass

    def bullet_velocity(self):
        for bullet in guardTowerBullets:
            n = len(guardTowerBullets) - 1

            bullet.guard_player_dx = (player.x - player.width) / 2 - (self.x - self.width) / 2
            bullet.guard_player_dy = (player.y - player.height) / 2 - (self.y - self.height) / 2
            bullet.angle = atan2(bullet.guard_player_dy, bullet.guard_player_dx)
            bullet.new_velocity = (3 * cos(bullet.angle), 3 * sin(bullet.angle))
            guardTowerBullets[n].velocity = bullet.new_velocity

    def shoot(self):

        if len(guard_shots) <= 8:
            now = pygame.time.get_ticks()
            if now - self.last >= 1500:
                self.last = now
                self.start_shoot()

        if len(guard_shots) > 8:

            now = pygame.time.get_ticks()
            if now - self.last >= 4000:
                self.last = now
                del guard_shots[:]

    def start_shoot(self):

        guardTowerBullets.append(Bullet(self.x, self.y))
        self.bullet_velocity()
        guardTowerShots.append([])

    def bullet_change(self):
        for bullet in guardTowerBullets:

            if bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > \
                    player.hitbox[1]:
                if bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox[0] + \
                        player.hitbox[2]:
                    player.shot()

                    if player.health == 0:
                        pass
                        message_to_screen("You lost", red, player.x, player.y, size="medium")
                        pygame.display.update()
                        pygame.quit()

                    guardTowerBullets.pop(guardTowerBullets.index(bullet))

            if screen_width > bullet.x > 0:

                n = 0
                while n <= len(guardTowerBullets) - 1:
                    guardTowerBullets[n].x += guardTowerBullets[n].velocity[0]
                    guardTowerBullets[n].y += guardTowerBullets[n].velocity[1]
                    n += 1

                if screen_width < bullet.x or bullet.x < 0:
                    guardTowerBullets.pop(guardTowerBullets.index(bullet))

                if screen_height < bullet.y or bullet.y < 0:
                    try:
                        guardTowerBullets.pop(guardTowerBullets.index(bullet))

                    except ValueError:
                        pass

            else:
                try:
                    guardTowerBullets.pop(guardTowerBullets.index(bullet))

                except ValueError:
                    pass


warden_bullets = []
wardens = []
warden_shots = []
wardens_killed = []

class Warden(Character, pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health
        self.speed = .5
        self.hitbox = (self.x - 8, self.y, 90, 90)
        self.last = pygame.time.get_ticks()
        self.shooting_cooldown = 200
        self.loading_cooldown = 200

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
            message_to_screen("You lost", red, player.x, player.y, size="medium")
            pygame.display.update()
            time.sleep(3)
            pygame.quit()

        else:
            pass

        self.hitbox = (self.x - 10, self.y, 90, 80)

        # HEALTHBAR
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

    def bullet_velocity(self, change_x, change_y):
        for bullet in warden_bullets:
            n = len(warden_bullets) - 1

            bullet.guard_player_dx = (player.x - player.width) / 2 - (self.x - self.width) / 2
            bullet.guard_player_dy = (player.y - player.height) / 2 - (self.y - self.height) / 2
            bullet.angle = atan2(bullet.guard_player_dy, bullet.guard_player_dx)
            bullet.new_velocity = (warden_bullets[n].speed * cos(bullet.angle), warden_bullets[n].speed * sin(bullet.angle))
            warden_bullets[n].velocity = bullet.new_velocity

    def shoot(self):

        if len(warden_shots) <= 8:
            now = pygame.time.get_ticks()
            if now - self.last >= 1500:
                self.last = now
                self.start_shoot()

        if len(warden_shots) > 8:

            now = pygame.time.get_ticks()
            if now - self.last >= 4000:
                self.last = now
                del warden_shots[:]

    def start_shoot(self):

        if self.left:
            warden_bullets.append(Bullet(self.x, self.y + 75))
            self.bullet_velocity(0, 75)
            warden_shots.append([])

        if self.right:
            warden_bullets.append(Bullet(self.x + 57, self.y + 7))
            self.bullet_velocity(57, 7)
            warden_shots.append([])

        if self.up:
            warden_bullets.append(Bullet(self.x + 7, self.y))
            self.bullet_velocity(7, 0)
            warden_shots.append([])

        if self.down:

            warden_bullets.append(Bullet(self.x + 75, self.y + 57))
            self.bullet_velocity(75, 57)
            warden_shots.append([])

        else:

            pass

    def bullet_change(self):

        for bullet in warden_bullets:

            if bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > \
                    player.hitbox[1]:
                if bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox[0] + \
                        player.hitbox[2]:
                    player.shot()

                    if player.health == 0:
                        pass
                        message_to_screen("You lost", red, player.x, player.y, size="medium")
                        pygame.display.update()
                        pygame.quit()

                    warden_bullets.pop(warden_bullets.index(bullet))

            if screen_width > bullet.x > 0:

                n = 0
                while n <= len(warden_bullets) - 1:
                    warden_bullets[n].x += warden_bullets[n].velocity[0]
                    warden_bullets[n].y += warden_bullets[n].velocity[1]
                    n += 1

                if screen_width < bullet.x or bullet.x < 0:
                    warden_bullets.pop(warden_bullets.index(bullet))

                if screen_height < bullet.y or bullet.y < 0:
                    try:
                        warden_bullets.pop(warden_bullets.index(bullet))

                    except ValueError:
                        pass

            else:
                try:
                    warden_bullets.pop(warden_bullets.index(bullet))

                except ValueError:
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
        self.radius = 3
        self.color = black
        self.speed = 15


def guardsKilled():
    if level_list[0] == 1:
        message_to_screen("Guards Killed: " + str(len(guards_killed)) + "/7", red, 1090, 20, "small")

    if level_list[0] == 2:
        message_to_screen("Guards Towers Killed: " + str(len(guardTowersKilled)) + "/2", red, 1050, 20, "small")

    if level_list[0] == 3:
        message_to_screen("Wardens Towers Killed: " + str(len(wardens_killed)) + "/1", red, 1030, 20, "small")


player = Player(200, 200, 83, 55, 'Prisoner', 10)

level_list = [1, 0]

if level_list[0] == 1:
    level_list[1] = pygame.image.load("level_1.png")


def redraw():
    if level_list[0] == 1 and len(guards_killed) >= 6:
        if player.x == 1100:
            player.x = 75
            player.y = 255

            level_list[0] += 1
            level_list[1] = pygame.image.load("level_" + str(level_list[0]) + ".png")

            player.left = False
            player.right = True
            player.down = False
            player.up = False

        else:
            pass

    if level_list[0] == 2 and len(guardTowersKilled) >= 2:

        if player.x == 900:
            player.x = 75
            player.y = 255

            level_list[0] += 1
            level_list[1] = pygame.image.load("level_" + str(level_list[0]) + ".png")

            player.left = False
            player.right = True
            player.down = False
            player.up = False

    if level_list[0] == 3 and len(wardens_killed) >= 1:

        if player.x == 900:
            player.x = 75
            player.y = 255

            level_list[0] += 1
            level_list[1] = pygame.image.load("level_" + str(level_list[0]) + ".png")

            player.left = False
            player.right = True
            player.down = False
            player.up = False

    if level_list[0] == 4:

        if player.x == 600:
            message_to_screen("You won", green, player.x, player.y, size="medium")
            pygame.display.update()
            time.sleep(3)
            pygame.quit()

    win.blit(level_list[1], (0, 0))
    player.draw()
    for i in player_bullets:
        i.draw()

    guardsKilled()
    for c in guards:
        if len(guards_killed) <= 6 and level_list[0] == 1:
            c.chase()
            c.draw()
            c.shoot()
            c.bullet_change()

        else:
            pass

    for i in guard_bullets:
        i.draw()

    for c in wardens:
        if len(wardens_killed) <= 0 and level_list[0] == 3:
            c.chase()
            c.draw()
            c.shoot()
            c.bullet_change()

        else:
            pass

    for i in warden_bullets:
        i.draw()


    for c in guardTowers:
        if len(guardTowersKilled) <= 1 and level_list[0] == 2:
            c.draw()
            c.shoot()
            c.bullet_change()
        else:
            pass

    for i in guardTowerBullets:
        i.draw()

    pygame.display.update()


def levelRestrictions():
    if level_list[0] == 1:
        if keys[pygame.K_a] and player.x > 0 + 4:
            player.x -= player.speed
            player.left = True
            player.right = False
            player.down = False
            player.up = False

        if keys[pygame.K_d] and player.x < screen_width - player.height - 25:
            player.x += player.speed
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        if keys[pygame.K_w] and player.y > 230:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 300:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False

    if level_list[0] == 2:
        if keys[pygame.K_a] and player.x > 0 + 225:
            player.x -= player.speed
            player.left = True
            player.right = False
            player.down = False
            player.up = False

        if keys[pygame.K_d] and player.x < screen_width - player.height - 225:
            player.x += player.speed
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        if keys[pygame.K_w] and player.y > 200:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 350:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False

    if level_list[0] == 3:
        if keys[pygame.K_a] and player.x > 0 + 225:
            player.x -= player.speed
            player.left = True
            player.right = False
            player.down = False
            player.up = False

        if keys[pygame.K_d] and player.x < screen_width - player.height - 225:
            player.x += player.speed
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        if keys[pygame.K_w] and player.y > 200:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 350:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False

    if level_list[0] == 4:

        if keys[pygame.K_a] and player.x > 0 + 225:
            player.x -= player.speed
            player.left = True
            player.right = False
            player.down = False
            player.up = False

        if keys[pygame.K_d] and player.x < screen_width - player.height - 225:
            player.x += player.speed
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        if keys[pygame.K_w] and player.y > 200:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 350:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False


clock = pygame.time.Clock()
run = True

# game_intro()
# how_to()
while run:
    global n

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_r]:
            del shots[:]
            player.loaded = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(player_bullets) < 6:

                loaded = True
                if len(shots) >= 6:
                    player.loaded = False

                player.bulletVelCalc()

    if len(guards) == 0 and level_list[0] == 1:
        guards.append(Mob(1200, 200, 82, 61, 'GuardGun', 10))

    if len(guardTowers) == 0 and level_list[0] == 2:
        guardTowers.append(GuardTower(715, 555, 82, 61, 10))
        guardTowers.append(GuardTower(715, 60, 82, 61, 10))

    if len(wardens) == 0 and level_list[0] == 3:
        wardens.append(Warden(980, 300, 82, 61, 'GuardGun', 10))

    g = 0
    gt = 0
    gt_2 = 1
    for bullet in player_bullets:
        if level_list[0] == 1:
            try:
                if bullet.y - bullet.radius < guards[g].hitbox[1] + guards[g].hitbox[3] and bullet.y + bullet.radius > \
                        guards[g].hitbox[1]:
                    if bullet.x + bullet.radius > guards[g].hitbox[0] and bullet.x - bullet.radius < guards[g].hitbox[0] + \
                            guards[g].hitbox[2]:

                        guards[g].shot()
                        for guard in guards:
                            if guards[g].health == 0:
                                guards_killed.append([])
                                guards.pop(guards.index(guard))

                        player_bullets.pop(player_bullets.index(bullet))
            except IndexError:
                pass

        if level_list[0] == 2:
            try:
                print(guardTowers)
                if bullet.y - bullet.radius < guardTowers[gt].hitbox[1] + guardTowers[gt].hitbox[3] and bullet.y + bullet.radius > \
                        guardTowers[gt].hitbox[1]:
                    if bullet.x + bullet.radius > guardTowers[gt].hitbox[0] and bullet.x - bullet.radius < guardTowers[gt].hitbox[
                        0] + \
                            guardTowers[gt].hitbox[2]:

                        guardTowers[gt].shot()

                        if guardTowers[gt].health == 0:
                            guardTowersKilled.append([])
                            guardTowers.pop(gt)

                        player_bullets.pop(player_bullets.index(bullet))


                if bullet.y - bullet.radius < guardTowers[gt_2].hitbox[1] + guardTowers[gt_2].hitbox[3] and bullet.y + bullet.radius > \
                        guardTowers[gt_2].hitbox[1]:
                    if bullet.x + bullet.radius > guardTowers[gt_2].hitbox[0] and bullet.x - bullet.radius < guardTowers[gt_2].hitbox[
                        0] + \
                            guardTowers[gt_2].hitbox[2]:

                        guardTowers[gt_2].shot()

                        if guardTowers[gt_2].health == 0:
                            guardTowersKilled.append([])
                            guardTowers.pop(gt_2)

                        player_bullets.pop(player_bullets.index(bullet))

            except IndexError:
                pass

        if level_list[0] == 3:
            try:
                if bullet.y - bullet.radius < wardens[g].hitbox[1] + wardens[g].hitbox[3] and bullet.y + bullet.radius > \
                        wardens[g].hitbox[1]:
                    if bullet.x + bullet.radius > wardens[g].hitbox[0] and bullet.x - bullet.radius < wardens[g].hitbox[0] + \
                            wardens[g].hitbox[2]:

                        wardens[g].shot()
                        for warden in wardens:
                            if wardens[g].health == 0:
                                wardens_killed.append([])
                                wardens.pop(wardens.index(warden))

                        player_bullets.pop(player_bullets.index(bullet))
            except IndexError:
                pass

        if screen_width > bullet.x > 0:

            n = 0
            while n <= len(player_bullets) - 1:
                player_bullets[n].x += player_bullets[n].velocity[0]
                player_bullets[n].y += player_bullets[n].velocity[1]
                n += 1

            if screen_width < bullet.x or bullet.x < 0:
                player_bullets.pop(player_bullets.index(bullet))

            if screen_height < bullet.y or bullet.y < 0:
                try:
                    player_bullets.pop(player_bullets.index(bullet))

                except ValueError:
                    pass

        else:
            try:
                player_bullets.pop(player_bullets.index(bullet))

            except ValueError:
                pass

    levelRestrictions()
    redraw()
    clock.tick(60)

pygame.quit()
