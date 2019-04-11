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


def message_to_screen(msg, color, y_dispalce=0, size = "small"):
    textsurf, textrect = text_objects(msg, color, size)
    textrect.center = (screen_width/2), (screen_height/2) + y_dispalce
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
        message_to_screen("Welcome to Rerun",
                          green,
                          -100)
        message_to_screen("The objective of this game is to escape from the prison",
                          white,
                          -30)
        message_to_screen("You need to fight your way through each level without getting caught or shot",
                          white,
                          10)
        message_to_screen("If you get caught or shot, you lose",
                          white,
                          50)
        message_to_screen("Press c to continue or q to quit",
                          red,
                          180,
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
        message_to_screen("Instructions",
                          green,
                          -100,
                          "large")
        message_to_screen("Press W to move up, A to move left, S to move down, and D to move right",
                          white,
                          -30)
        message_to_screen("Using the mouse to shoot, and press R to recoil",
                          white,
                          10)
        message_to_screen("GLHF!",
                          white,
                          50)
        message_to_screen("Press p to play or q to quit",
                          red,
                          180,
                          "small")
        pygame.display.update()


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
        self.hitbox = (self.x - 8, self.y, 90, 90)

    def shot(self):
        if self.health > 0:
            self.health -= 1
        else:
            pass

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

        self.hitbox = (self.x - 10, self.y, 90, 80)

        # HEALTHBAR
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))



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


class Click:
    def __init__(self, mouse_pos):
        self.mouse_pos = mouse_pos


guard = Mob(1250, 255, 82, 61, 'GuardGun', 6)
player = Player(200, 200, 82, 49, 'prisoner', 6)
b = Bullet(player.x, player.y)
bullets = []
guards = []
clicks = []
shots = []
stop = []

def redraw():
    win.blit(bg, (0, 0))
    player.draw()
    #guard.chase()
    #guard.draw()
    lvlup()
    for i in bullets:
        i.draw()
    for c in guards:
        c.chase()
        c.draw()
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

game_intro()
how_to()
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

                            if clicks[s][0] <= (player.x + player.height/2 + player.width/2) - 100:
                                if clicks[s][1] <= (player.y + player.height/2 + player.width/2) + 200:
                                    if clicks[s][1] >= (player.y + player.height/2 + player.width/2) - 200:
                                        bullets.append(Bullet(player.x, player.y + 75))
                                        bullet_velocity(0, 75)
                                        shots.append([])
                                        break
                            break

                        if player.right:

                            if clicks[s][0] >= (player.x + player.height/2 + player.width/2) + 100:
                                if clicks[s][1] >= (player.y + player.height/2 + player.width/2) - 200:
                                    if clicks[s][1] <= (player.y + player.height/2 + player.width/2) + 200:
                                        bullets.append(Bullet(player.x + 57, player.y + 7))
                                        bullet_velocity(57, 7)
                                        shots.append([])
                                        break
                            break

                        if player.up:
                            if clicks[s][1] <= (player.y + player.height/2 + player.width/2) - 100:
                                if clicks[s][0] >= (player.x + player.height/2 + player.width/2) - 200:
                                    if clicks[s][0] <= (player.x + player.height/2 + player.width/2) + 200:
                                        bullets.append(Bullet(player.x + 7, player.y))
                                        bullet_velocity(7, 0)
                                        shots.append([])
                                        break
                            break

                        if player.down:
                            if clicks[s][1] >= player.y + 200:
                                if clicks[s][0] >= (player.x + player.height/2 + player.width/2) - 200:
                                    if clicks[s][0] <= (player.x + player.height/2 + player.width/2) + 200:
                                        bullets.append(Bullet(player.x + 75, player.y + 57))
                                        bullet_velocity(75, 57)
                                        shots.append([])
                                        break
                            break

                        if clicks[s][0] >= (player.x + player.height / 2 + player.width / 2) + 100:
                            if clicks[s][1] >= (player.y + player.height / 2 + player.width / 2) - 200:
                                if clicks[s][1] <= (player.y + player.height / 2 + player.width / 2) + 200:
                                    bullets.append(Bullet(player.x + 57, player.y + 7))
                                    bullet_velocity(57, 7)
                                    shots.append([])
                                    break
                        break

                    else:
                        pass

    if len(guards) <= 0:
        guards.append(Mob(1250, 400, 82, 61, 'GuardGun', 6))

    g = 0
    for bullet in bullets:
        try:
            if bullet.y - bullet.radius < guards[g].hitbox[1] + guards[g].hitbox[3] and bullet.y + bullet.radius > guards[g].hitbox[1]:
                if bullet.x + bullet.radius > guards[g].hitbox[0] and bullet.x - bullet.radius < guards[g].hitbox[0] + guards[g].hitbox[2]:

                    guards[g].shot()
                    for guard in guards:
                        print(guards[g].health)

                        if guards[g].health == 0:
                            guards.pop(guards.index(guard))

                    bullets.pop(bullets.index(bullet))
        except IndexError:
            pass

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
                try:
                    bullets.pop(bullets.index(bullet))

                except ValueError:
                    pass



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
