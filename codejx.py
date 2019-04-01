import pygame
import time

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


bg = pygame.image.load('JailCell1.jpg')
lvl1 = pygame.image.load('lvl1.jpg')

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
class Player(pygame.sprite.Sprite):
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
        self.image = pygame.image.load('player0.jpg')

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.lookUp = [pygame.image.load(self.name + '0.jpg')]
        self.lookDown = [pygame.image.load(self.name + '180.jpg')]
        self.lookLeft = [pygame.image.load(self.name + '270.jpg')]
        self.lookRight = [pygame.image.load(self.name + '90.jpg')]
        self.lookIdle = [pygame.image.load(self.name + '90.jpg')]

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


player = Player(75, 255, 40, 60, 'player')


# classifying Guards
class Guard(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name):
        pygame.sprite.Sprite.__init__(self)
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

Guard = Guard(1250, 255, 40, 60, 'Guard')


# update positions
def prelvlwindow():
    win.blit(bg, (0, 0))
    player.draw()
    Guard.chase()
    Guard.draw()
    lvlup()
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

        if keys[pygame.K_UP] and player.y > 150:
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

        prelvlwindow()
        clock.tick(60)


# game starts here
prelevel()


pygame.quit()
