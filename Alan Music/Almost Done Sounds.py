import pygame
import time  # Imported to pause the game before exiting
from math import atan2, sin, cos  # Imported to calculate bullet to player angles
weapon = 0
ammoleft = 96
able = True
pygame.init()  # Initialize all imported Pygame modules

# Defining colours with hexadecimal values
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (210, 210, 210)

# Defining sounds
bsound = pygame.mixer.Sound("Button1.wav")
selfdmg = pygame.mixer.Sound("selfdmg.wav")
reloadsound = pygame.mixer.Sound("reload.wav")
gunsound = pygame.mixer.Sound("gunsound.wav")
purchasesound = pygame.mixer.Sound("purchasesound.wav")
nocoinsound = pygame.mixer.Sound("nocoinsound.wav")
shopselect = pygame.mixer.Sound("shopselect.wav")

# defining different fonts which will be used in a function that allows us to display text in our game
smallfont = pygame.font.SysFont("comicsansms", 25)  # Small Comic Sans font
medfont = pygame.font.SysFont("comicsansms", 50)  # Medium Comic Sans font
largefont = pygame.font.SysFont("comicsansms", 80)  # Large Comic Sans font

# Defining variables for screen width and height
screen_width = 1200
screen_height = 600

# Using Pygame to create the window in which the game will be played in
win = pygame.display.set_mode((screen_width, screen_height))

# Setting the caption name for the game
pygame.display.set_caption("Limbo")


def text_objects(text, color, size):  # Defining text sizes
    if size == "small":
        textsurface = smallfont.render(text, True, color)
    elif size == "medium":
        textsurface = medfont.render(text, True, color)
    elif size == "large":
        textsurface = largefont.render(text, True, color)

    return textsurface, textsurface.get_rect()


def message_to_screen(msg, color, x, y, size):  # Used to show text on the screen
    textsurf, textrect = text_objects(msg, color, size)
    textrect.center = (x, y)
    win.blit(textsurf, textrect)

start = pygame.image.load('start.png')
info = pygame.image.load('info.png')
ak47 = pygame.image.load("AK47.png")
ammo = pygame.image.load("Ammo.png")
sniper = pygame.image.load('Sniper.png')
vest = pygame.image.load('Vest.png')
locked = pygame.image.load('Locked.png')


def game_intro():
    startbuttons()
    infobutton()
    pygame.display.update()


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, black)
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


def bottons():
    win.blit(start, (0, 0))
    greyButton1.draw(win, black)
    greyButton2.draw(win, black)


def instruction():
    win.blit(info, (0, 0))
    greyButton3.draw(win, black)


level3 = pygame.image.load("Level_3.png")


def shopBut():
    win.blit(level3, (0, 0))
    shopButton1.draw(win, black)
    shopButton2.draw(win, black)
    pygame.display.update()


def shopak47():
    win.blit(ak47, (0, 0))
    greyButton3.draw(win, black)
    buy.draw(win, black)
    sniperbut.draw(win, black)
    vestbut.draw(win, black)
    ammobut.draw(win, black)
    lockedbut.draw(win, black)
    message_to_screen("Coins: " + str(player_gold[0]), white, 130, 75, "small")
    message_to_screen("Bullets left: " + str(stock[0]) + "/" + str(ammoleft), white, 1050, 75, "small")
    pygame.display.update()


def shopsniper():
    win.blit(sniper, (0, 0))
    greyButton3.draw(win, black)
    buy.draw(win, black)
    ak47but.draw(win, black)
    vestbut.draw(win, black)
    ammobut.draw(win, black)
    lockedbut.draw(win, black)
    message_to_screen("Coins: " + str(player_gold[0]), white, 130, 75, "small")
    message_to_screen("Bullets left: " + str(stock[0]) + "/" + str(ammoleft), white, 1050, 75, "small")
    pygame.display.update()


def shopvest():
    win.blit(vest, (0, 0))
    greyButton3.draw(win, black)
    buy.draw(win, black)
    ak47but.draw(win, black)
    sniperbut.draw(win, black)
    ammobut.draw(win, black)
    lockedbut.draw(win, black)
    message_to_screen("Coins: " + str(player_gold[0]), white, 130, 75, "small")
    message_to_screen("Bullets left: " + str(stock[0]) + "/" + str(ammoleft), white, 1050, 75, "small")
    pygame.display.update()


def shopammo():
    win.blit(ammo, (0, 0))
    greyButton3.draw(win, black)
    buy.draw(win, black)
    ak47but.draw(win, black)
    vestbut.draw(win, black)
    sniperbut.draw(win, black)
    lockedbut.draw(win, black)
    message_to_screen("Coins: " + str(player_gold[0]), white, 130, 75, "small")
    message_to_screen("Bullets left: " + str(stock[0]) + "/" + str(ammoleft), white, 1050, 75, "small")
    pygame.display.update()


def shoplocked():
    win.blit(locked, (0, 0))
    greyButton3.draw(win, black)
    buy.draw(win, black)
    ak47but.draw(win, black)
    vestbut.draw(win, black)
    ammobut.draw(win, black)
    sniperbut.draw(win, black)
    message_to_screen("Coins: " + str(player_gold[0]), white, 130, 75, "small")
    message_to_screen("Bullets left: " + str(stock[0]) + "/" + str(ammoleft), white, 1050, 75, "small")
    pygame.display.update()


run = True
greyButton1 = button(grey, 116, 416, 250, 100, 'Start')
greyButton2 = button(grey, 738, 418, 250, 100, 'Info')
greyButton3 = button(grey, 0, 500, 250, 100, 'Back')    # back botton
shopButton1 = button(grey, 950, 0, 250, 100, 'Shop')
shopButton2 = button(grey, 950, 500, 250, 100, 'Exit')
ak47but = button(grey, 875, 202, 320, 75, 'AK47')
sniperbut = button(grey, 875, 282, 320, 75, 'SNIPER')
vestbut = button(grey, 875, 362, 320, 75, 'VEST')
ammobut = button(grey, 875, 442, 320, 75, 'AMMO')
lockedbut = button(grey, 875, 522, 320, 74, 'LOCKED')
buy = button(grey, 475, 500, 250, 100, 'BUY')


def startbuttons():
    global run
    while run:
        bottons()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if greyButton1.isOver(pos):
                    bsound.play()
                    print("Game Starts")
                    game_loop()

                if greyButton2.isOver(pos):
                    bsound.play()
                    print("Instructions")
                    infobutton()
            if event.type == pygame.MOUSEMOTION:
                if greyButton1.isOver(pos):
                    greyButton1.color = red

                elif greyButton2.isOver(pos):
                    greyButton2.color = green

                else:
                    greyButton1.color = grey
                    greyButton2.color = grey


def infobutton():
    global run
    while run:
        instruction()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if greyButton3.isOver(pos):
                    bsound.play()
                    startbuttons()
            if event.type == pygame.MOUSEMOTION:
                if greyButton3.isOver(pos):
                    greyButton3.color = green

                else:
                    greyButton3.color = grey


def shop():
    global run
    while run:
        shopBut()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shopButton1.isOver(pos):
                    bsound.play()
                    shop1()

                if shopButton2.isOver(pos):
                    bsound.play()
                    player.x = 75
                    player.y = 255

                    level_list[0] += 1  # Increase the level number
                    level_list[1] = pygame.image.load(
                        "level_" + str(level_list[0]) + ".png")  # Level image sent to list

                    # Start the player looking right
                    player.left = False
                    player.right = True
                    player.down = False
                    player.up = False
                    run = False
            if event.type == pygame.MOUSEMOTION:
                if shopButton1.isOver(pos):
                    shopButton1.color = green
                elif shopButton2.isOver(pos):
                    shopButton2.color = red

                else:
                    shopButton1.color = grey
                    shopButton2.color = grey


def shop1():    #ak47
    global run
    while run:
        shopak47()

        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if greyButton3.isOver(pos):
                    bsound.play()
                    shop()
                elif buy.isOver(pos):

                    if player_gold[0] - 250 >= 0:
                        player_gold[0] -= 250
                        global weapon
                        weapon = 1
                        purchasesound.play()
                        print("Item Bought")
                    else:
                        message_to_screen("NOT ENOUGH COINS", red, 600, 300, "medium" )
                        nocoinsound.play()
                        pygame.display.update()
                        time.sleep(1)
                        pygame.display.update()
                elif sniperbut.isOver(pos):
                    shop2()
                    shopselect.play()
                elif vestbut.isOver(pos):
                    shop3()
                    shopselect.play()
                elif ammobut.isOver(pos):
                    shop4()
                    shopselect.play()
                elif lockedbut.isOver(pos):
                    shop5()
                    shopselect.play()
                else:
                    pass

            if event.type == pygame.MOUSEMOTION:
                if greyButton3.isOver(pos):
                    greyButton3.color = green
                elif buy.isOver(pos):
                    buy.color = green
                elif sniperbut.isOver(pos):
                    sniperbut.color = green
                elif vestbut.isOver(pos):
                    vestbut.color = green
                elif ammobut.isOver(pos):
                    ammobut.color = green
                elif lockedbut.isOver(pos):
                    lockedbut.color = green
                else:
                    greyButton3.color = grey
                    buy.color = grey
                    sniperbut.color = grey
                    vestbut.color = grey
                    ammobut.color = grey
                    lockedbut.color = grey


def shop2():     # sniper
    global run
    while run:
        shopsniper()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if greyButton3.isOver(pos):
                    bsound.play()
                    shop()
                elif buy.isOver(pos):
                    if player_gold[0] - 250 >= 0:
                        player_gold[0] -= 250
                        global weapon
                        weapon = 2
                        purchasesound.play()
                        print("Item Bought")
                    else:
                        message_to_screen("NOT ENOUGH COINS", red, 600, 300, "medium" )
                        nocoinsound.play()
                        pygame.display.update()
                        time.sleep(1)
                        pygame.display.update()
                elif ak47but.isOver(pos):
                    shopselect.play()
                    shop1()
                elif vestbut.isOver(pos):
                    shopselect.play()
                    shop3()
                elif ammobut.isOver(pos):
                    shopselect.play()
                    shop4()
                elif lockedbut.isOver(pos):
                    shopselect.play()
                    shop5()
                else:
                    pass

            if event.type == pygame.MOUSEMOTION:
                if greyButton3.isOver(pos):
                    greyButton3.color = green
                elif buy.isOver(pos):
                    buy.color = green
                elif ak47but.isOver(pos):
                    ak47but.color = green
                elif vestbut.isOver(pos):
                    vestbut.color = green
                elif ammobut.isOver(pos):
                    ammobut.color = green
                elif lockedbut.isOver(pos):
                    lockedbut.color = green
                else:
                    greyButton3.color = grey
                    buy.color = grey
                    ak47but.color = grey
                    vestbut.color = grey
                    ammobut.color = grey
                    lockedbut.color = grey


def shop3():     # vest
    global run
    while run:
        shopvest()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if greyButton3.isOver(pos):
                    bsound.play()
                    shop()
                elif buy.isOver(pos):
                    if player_gold[0] - 250 >= 0:
                        player_gold[0] -= 250
                        global weapon
                        weapon = 3
                        purchasesound.play()
                        print("Item Bought")
                    else:
                        message_to_screen("NOT ENOUGH COINS", red, 600, 300, "medium" )
                        nocoinsound.play()
                        pygame.display.update()
                        time.sleep(1)
                        pygame.display.update()
                elif ak47but.isOver(pos):
                    shopselect.play()
                    shop1()
                elif sniperbut.isOver(pos):
                    shopselect.play()
                    shop2()
                elif ammobut.isOver(pos):
                    shopselect.play()
                    shop4()
                elif lockedbut.isOver(pos):
                    shopselect.play()
                    shop5()
                else:
                    pass

            if event.type == pygame.MOUSEMOTION:
                if greyButton3.isOver(pos):
                    greyButton3.color = green
                elif buy.isOver(pos):
                    buy.color = green
                elif ak47but.isOver(pos):
                    ak47but.color = green
                elif sniperbut.isOver(pos):
                    sniperbut.color = green
                elif ammobut.isOver(pos):
                    ammobut.color = green
                elif lockedbut.isOver(pos):
                    lockedbut.color = green
                else:
                    greyButton3.color = grey
                    buy.color = grey
                    ak47but.color = grey
                    sniperbut.color = grey
                    ammobut.color = grey
                    lockedbut.color = grey


def shop4():  # ammo
    global run
    while run:
        shopammo()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if greyButton3.isOver(pos):
                    bsound.play()
                    shop()
                elif buy.isOver(pos):
                    if player_gold[0] - 50 >= 0:
                        player_gold[0] -= 50
                        if weapon == 1:
                            global ammoleft
                            stock[0] += ammoleft
                            stock[0] += 50
                            ammoleft = 0
                        else:
                            ammoleft += 50
                        print("Item Bought")
                        purchasesound.play()
                    else:
                        message_to_screen("NOT ENOUGH COINS", red, 600, 300, "medium" )
                        nocoinsound.play()
                        pygame.display.update()
                        time.sleep(1)
                        pygame.display.update()
                elif ak47but.isOver(pos):
                    shopselect.play()
                    shop1()
                elif sniperbut.isOver(pos):
                    shopselect.play()
                    shop2()
                elif vestbut.isOver(pos):
                    shopselect.play()
                    shop3()
                elif lockedbut.isOver(pos):
                    shopselect.play()
                    shop5()
                else:
                    pass

            if event.type == pygame.MOUSEMOTION:
                if greyButton3.isOver(pos):
                    greyButton3.color = green
                elif buy.isOver(pos):
                    buy.color = green
                elif ak47but.isOver(pos):
                    ak47but.color = green
                elif sniperbut.isOver(pos):
                    sniperbut.color = green
                elif vestbut.isOver(pos):
                    vestbut.color = green
                elif lockedbut.isOver(pos):
                    lockedbut.color = green
                else:
                    greyButton3.color = grey
                    buy.color = grey
                    ak47but.color = grey
                    sniperbut.color = grey
                    vestbut.color = grey
                    lockedbut.color = grey


def shop5():
    global run
    while run:
        shoplocked()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if greyButton3.isOver(pos):
                    bsound.play()
                    shop()
                elif buy.isOver(pos):
                    print("Item Bought")
                    purchasesound.play()
                elif ak47but.isOver(pos):
                    shopselect.play()
                    shop1()
                elif sniperbut.isOver(pos):
                    shopselect.play()
                    shop2()
                elif vestbut.isOver(pos):
                    shopselect.play()
                    shop3()
                elif ammobut.isOver(pos):
                    shopselect.play()
                    shop4()
                else:
                    pass

            if event.type == pygame.MOUSEMOTION:
                if greyButton3.isOver(pos):
                    greyButton3.color = green
                elif buy.isOver(pos):
                    buy.color = green
                elif ak47but.isOver(pos):
                    ak47but.color = green
                elif sniperbut.isOver(pos):
                    sniperbut.color = green
                elif vestbut.isOver(pos):
                    vestbut.color = green
                elif ammobut.isOver(pos):
                    ammobut.color = green
                else:
                    greyButton3.color = grey
                    buy.color = grey
                    ak47but.color = grey
                    sniperbut.color = grey
                    vestbut.color = grey
                    ammobut.color = grey


player_bullets = []  # List that will hold all of the bullets for the player
shots = []  # List that will keep track of the number of shots the player has taken (for reloading the gun)

stock = []
stock.append([])
stock[0] = 6
clicks = []  # List that will hold all of the mouse positions
guard_bullets = []  # List that will hold all of the bullets for the guards
guards = []  # List that will hold all of the guard sprites
guard_shots = []  # List that will keep track of the number of shots the player has taken (for reloading the gun)
guards_killed = []  # List that keeps track of how many guards a player has killed


# Class that defines each click
class Click:
    def __init__(self, mouse_pos):
        self.mouse_pos = mouse_pos


# Class that defines all characters
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name  # Name of character. This is used to pull the character's corresponding image.
        self.x = x  # Starting x position of the character
        self.y = y  # Starting y position of the character
        self.width = width  # Width of character
        self.height = height  # Height of character

        # Starting directions
        self.left = False
        self.right = False
        self.down = False
        self.up = False

        # Loading images for each direction
        self.lookUp = pygame.image.load(self.name + '90.png')
        self.lookDown = pygame.image.load(self.name + '270.png')
        self.lookLeft = pygame.image.load(self.name + '180.png')
        self.lookRight = pygame.image.load(self.name + '0.png')
        self.lookIdle = pygame.image.load(self.name + '0.png')

        # Defining the center for the character
        self.rect = self.lookIdle.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self):
        # Drawing the character's direction to the screen

        if self.left:  # If direction is left
            win.blit(self.lookLeft, (self.x, self.y))
            self.hitbox = (self.x, self.y, self.height, self.width)

        elif self.right:  # If direction is right
            win.blit(self.lookRight, (self.x, self.y))
            self.hitbox = (self.x, self.y, self.height, self.width)

        elif self.down:  # If direction is down
            win.blit(self.lookDown, (self.x, self.y))
            self.hitbox = (self.x, self.y, self.width, self.height)

        elif self.up:  # If direction is up
            win.blit(self.lookUp, (self.x, self.y))
            self.hitbox = (self.x, self.y, self.width, self.height)

        else:  # If no direction has been assigned ("idle"/starting direction)
            win.blit(self.lookIdle, (self.x, self.y))

        # Defining the hitbox for a character
        self.hitbox = (self.x - 10, self.y, 90, 80)

        # Drawing the hitbox for a character
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))


class Player(Character, pygame.sprite.Sprite):  # Class that defines the player/prisoner
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)  # Calling __init__ from Character
        self.speed = 25  # Player speed
        self.loaded = True  # Player's gun is loaded
        self.alive = True  # Player is alive (health > 0)
        self.health = 10
        self.armour = 0
    # Function that determines the velocity (speed + direction) of the bullet
    def bullet_velocity(self, change_x, change_y):
        for bullet in player_bullets:  # For each bullet shot
            n = len(player_bullets) - 1

            bullet.mouse_position = pygame.mouse.get_pos()  # Find the mouse click's position

            # Find the distance between the bullet's position at time = 0 to the click's position
            bullet.mouse_player_dx = bullet.mouse_position[0] - (self.x + change_x)
            bullet.mouse_player_dy = bullet.mouse_position[1] - (self.y + change_y)

            # Calculate the angle between the initial position of the bullet and the click's position
            bullet.angle = atan2(bullet.mouse_player_dy, bullet.mouse_player_dx)

            # Calculate the velocity of the bullet using the speed and direction (angle)
            bullet.new_velocity = (player_bullets[n].speed * cos(bullet.angle), player_bullets[n].speed * sin(bullet.angle))

            # Change the initial velocity of the bullet to the final (calculated) velocity of the bullet
            # This is used later to show the bullet moving in the click's direction
            player_bullets[n].velocity = bullet.new_velocity

    def shot(self):  # Function that decreases health for a character when they're shot
        if self.health > 0:
            self.health -= 1
        else:
            pass

    def bulletVelCalc(self):
        # Calculating mouse position again, but this time to restrict where the player can shoot at
        mouse_positions = pygame.mouse.get_pos()

        # Create a value in a list for each click, but with the position of (0,0). This value will be updated
        # later for each click
        pos_none = (0, 0)
        clicks.append(Click(pos_none))
        print(mouse_positions)

        for click in clicks:
            s = len(clicks) - 1
            clicks[s] = mouse_positions  # Change the (0,0) position to the mouse click's position
            if self.loaded == True:  # If the gun is loaded

                if self.left:  # If the player is looking left

                    # Creating the restriction box
                    if clicks[s][0] <= (self.x + self.height / 2 + self.width / 2) - 100:
                        if clicks[s][1] <= (self.y + self.height / 2 + self.width / 2) + 200:
                            if clicks[s][1] >= (self.y + self.height / 2 + self.width / 2) - 200:
                                player_bullets.append(Bullet(self.x, self.y + 75))  # Create the bullet
                                gunsound.play()
                                self.bullet_velocity(0, 75)  # Give the bullet its velocity
                                # Add an element to the shots list that determines if the gun is loaded
                                shots.append([])
                                stock[0] -= 1
                                break
                    break

                if self.right:  # If the player is looking right

                    # Creating the restriction box
                    if clicks[s][0] >= (self.x + self.height / 2 + self.width / 2) + 100:
                        if clicks[s][1] >= (self.y + self.height / 2 + self.width / 2) - 200:
                            if clicks[s][1] <= (self.y + self.height / 2 + self.width / 2) + 200:
                                player_bullets.append(Bullet(self.x + 57, self.y + 7))  # Create the bullet
                                gunsound.play()
                                self.bullet_velocity(57, 7)  # Give the bullet its velocity
                                # Add an element to the shots list that determines if the gun is loaded
                                shots.append([])
                                stock[0] -= 1
                                break
                    break

                if self.up:  # If the player is looking up

                    # Creating the restriction box
                    if clicks[s][1] <= (self.y + self.height / 2 + self.width / 2) - 100:
                        if clicks[s][0] >= (self.x + self.height / 2 + self.width / 2) - 200:
                            if clicks[s][0] <= (self.x + self.height / 2 + self.width / 2) + 200:
                                player_bullets.append(Bullet(self.x + 7, self.y))  # Create the bullet
                                gunsound.play()
                                self.bullet_velocity(7, 0)  # Give the bullet its velocity
                                # Add an element to the shots list that determines if the gun is loaded
                                shots.append([])
                                stock[0] -= 1
                                break
                    break

                if self.down:  # If the player is looking down

                    # Creating the restriction box
                    if clicks[s][1] >= self.y + 200:
                        if clicks[s][0] >= (self.x + self.height / 2 + self.width / 2) - 200:
                            if clicks[s][0] <= (self.x + self.height / 2 + self.width / 2) + 200:
                                player_bullets.append(Bullet(self.x + 75, self.y + 57))  # Create the bullet
                                gunsound.play()
                                self.bullet_velocity(75, 57)  # Give the bullet its velocity
                                # Add an element to the shots list that determines if the gun is loaded
                                shots.append([])
                                stock[0] -= 1
                                break
                    break

                if self.lookIdle:  # If the player is in idle position

                    # Creating the restriction box
                    if clicks[s][0] >= (self.x + self.height / 2 + self.width / 2) + 100:
                        if clicks[s][1] >= (self.y + self.height / 2 + self.width / 2) - 200:
                            if clicks[s][1] <= (self.y + self.height / 2 + self.width / 2) + 200:
                                player_bullets.append(Bullet(self.x + 57, self.y + 7))  # Create the bullet
                                self.bullet_velocity(57, 7)  # Give the bullet its velocity
                                # Add an element to the shots list that determines if the gun is loaded
                                shots.append([])
                                stock[0] -= 1
                                break
                    break

        else:
            pass


class Mob(Character, pygame.sprite.Sprite):  # Class that defines each guard
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)  # Calling __init__ from Character
        self.health = health  # Guard health
        self.speed = 2.5  # Guard speed
        self.hitbox = (self.x - 8, self.y, 90, 90)  # Guard hitbox

        # Used to change how fast the guard can shoot
        self.last = pygame.time.get_ticks()
        self.shooting_cooldown = 200
        self.loading_cooldown = 200

    def chase(self):  # allows the guard to chase the player by comparing the player's x/y coordinates to the guard's

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

        # Drawing the hitbox for a character
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

    # Function that determines the velocity (speed + direction) of the bullet

    def shot(self):  # Function that decreases health for a character when they're shot
        if self.health > 0:
            if weapon == 2:
                self.health -= 2
            else:
                self.health -= 1
        else:
            pass

    def bullet_velocity(self):
        for bullet in guard_bullets:  # For each bullet shot
            n = len(guard_bullets) - 1

            # Find the distance between the player and the guard
            bullet.guard_player_dx = (player.x - player.width) / 2 - (self.x - self.width) / 2
            bullet.guard_player_dy = (player.y - player.height) / 2 - (self.y - self.height) / 2

            # Calculate the angle to the player
            bullet.angle = atan2(bullet.guard_player_dy, bullet.guard_player_dx)

            # Calculate and add the bullet velocity to each specific bullet's position in the list
            bullet.new_velocity = (guard_bullets[n].speed * cos(bullet.angle), guard_bullets[n].speed * sin(bullet.angle))
            guard_bullets[n].velocity = bullet.new_velocity

    def shoot(self):

        if len(guard_shots) <= 8:  # If guard has shot less than 8 times
            now = pygame.time.get_ticks()
            if now - self.last >= 1500:  # Wait 1.5 seconds
                self.last = now
                self.start_shoot()  # Shoot again

        if len(guard_shots) > 8:  # If guard has shot 8 or more times
            now = pygame.time.get_ticks()
            if now - self.last >= 4000:  # Wait 4 seconds
                self.last = now
                del guard_shots[:]  # Empty the list that keeps track of how many time the guard has shot

    def start_shoot(self):  # Function that shoots each bullet

        if self.left:  # If guard is looking left
            guard_bullets.append(Bullet(self.x, self.y + 75))
            self.bullet_velocity()
            guard_shots.append([])

        if self.right:  # If guard is looking right
            guard_bullets.append(Bullet(self.x + 57, self.y + 7))
            self.bullet_velocity()
            guard_shots.append([])

        if self.up:  # If guard is looking up
            guard_bullets.append(Bullet(self.x + 7, self.y))
            self.bullet_velocity()
            guard_shots.append([])

        if self.down:  # If guard is looking down
            guard_bullets.append(Bullet(self.x + 75, self.y + 57))
            self.bullet_velocity()
            guard_shots.append([])

        else:
            pass

    def bullet_change(self):  # Function that updates each bullet's position with the velocity calculated

        for bullet in guard_bullets:  # For each bullet

            # Bullet interaction with player's hitbox
            if bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > \
                    player.hitbox[1]:
                if bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox[0] + \
                        player.hitbox[2]:
                    player.shot()

                    # If player's health is 0, print a game over message to the screen and end the game
                    if player.health == 0 or player.health <= 0:
                        pass
                        message_to_screen("You lost", red, player.x, player.y, size="medium")
                        pygame.display.update()
                        time.sleep(3)
                        pygame.quit()

                    # Pop/delete the bullet after it hits a player
                    guard_bullets.pop(guard_bullets.index(bullet))
                    selfdmg.play()

            if screen_width > bullet.x > 0:

                n = 0
                while n <= len(guard_bullets) - 1:
                    # For each bullet, constantly change its x and y position as determined by the calculated velocity
                    guard_bullets[n].x += guard_bullets[n].velocity[0]
                    guard_bullets[n].y += guard_bullets[n].velocity[1]
                    n += 1

                # If the bullet leaves the screen, pop the bullet
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

guardTowerBullets = []  # List that holds each bullet for a tower
guardTowers = []  # List that keeps track of how many towers are in the game
guardTowersKilled = []  # List that keeps track of how many towers have been killed

class GuardTower(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, health):
        pygame.sprite.Sprite.__init__(self)

        self.x = x  # Starting x position of the tower
        self.y = y  # Starting y position of the tower
        self.width = width  # Width of tower
        self.height = height  # Height of tower
        self.health = health  # Health of tower
        self.hitbox = (self.x - 10, self.y, self.width, self.height)  # Tower hitbox

        # Used to change how fast the guard tower can shoot
        self.last = pygame.time.get_ticks()
        self.shooting_cooldown = 200
        self.loading_cooldown = 200

    def draw(self):

        # Draw the tower's hitbox
        pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

    def shot(self):  # Function that decreases health for a character when they're shot
        if self.health > 0:
            if weapon == 2:
                self.health -= 2
            else:
                self.health -= 1
        else:
            pass

    # Function that determines the velocity (speed + direction) of the bullet
    def bullet_velocity(self):
        for bullet in guardTowerBullets:  # For each bullet shot
            n = len(guardTowerBullets) - 1

            # Find the distance between the player and the tower
            bullet.guard_player_dx = (player.x - player.width) / 2 - (self.x - self.width) / 2
            bullet.guard_player_dy = (player.y - player.height) / 2 - (self.y - self.height) / 2

            # Calculate the angle to the player
            bullet.angle = atan2(bullet.guard_player_dy, bullet.guard_player_dx)

            # Calculate and add the bullet velocity to each specific bullet's position in the list
            bullet.new_velocity = (3 * cos(bullet.angle), 3 * sin(bullet.angle))
            guardTowerBullets[n].velocity = bullet.new_velocity

    def shoot(self):
        # Wait 2 seconds before shooting
        now = pygame.time.get_ticks()
        if now - self.last >= 2000:
            self.last = now
            self.start_shoot()  # Shoot a bullet in start_shoot()

    def start_shoot(self):
        #  Shoot a bullet and add it to the bullets list
        guardTowerBullets.append(Bullet(self.x, self.y))
        self.bullet_velocity()  # Calculate the velocity of the bullet

    def bullet_change(self):  # Function that updates each bullet's position with the velocity calculated
        for bullet in guardTowerBullets:  # For each bullet

            # Bullet interaction with player's hitbox
            if bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > \
                    player.hitbox[1]:
                if bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox[0] + \
                        player.hitbox[2]:
                    player.shot()

                    # If player's health is 0, print a game over message to the screen and end the game
                    if player.health == 0:  #
                        pass
                        message_to_screen("You lost", red, player.x, player.y, size="medium")
                        pygame.display.update()
                        pygame.quit()

                    guardTowerBullets.pop(guardTowerBullets.index(bullet))

            # If the bullet leaves the screen, pop the bullet
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


warden_bullets = []  # List that holds all of the bullets the warden shoots
wardens = []  # List that holds the warden sprite
warden_shots = []  # List that keeps track of how many bullets the warden has shot
wardens_killed = []  # List that keeps track of how many wardens have been killed

class Warden(Character, pygame.sprite.Sprite):  # Class that defines the warden
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)  # Calling __init__ from Character
        self.health = health  # Warden health
        self.speed = .5  # Warden speed
        self.hitbox = (self.x - 8, self.y, 90, 90)  # Warden hitbox

        # Used to change how fast the guard can shoot
        self.last = pygame.time.get_ticks()
        self.shooting_cooldown = 200
        self.loading_cooldown = 200

    def chase(self):  # allows the warden to chase the player by comparing the player's x/y coordinates to the warden's

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

    # Function that determines the velocity (speed + direction) of the bullet

    def shot(self):  # Function that decreases health for a character when they're shot
        if self.health > 0:
            if weapon == 2:
                self.health -= 2
            else:
                self.health -= 1
        else:
            pass

    def bullet_velocity(self, change_x, change_y):
        for bullet in warden_bullets:  # For each bullet shot
            n = len(warden_bullets) - 1

            # Find the distance between the player and the warden
            bullet.guard_player_dx = (player.x - player.width) / 2 - (self.x - self.width) / 2
            bullet.guard_player_dy = (player.y - player.height) / 2 - (self.y - self.height) / 2

            # Calculate the angle to the player
            bullet.angle = atan2(bullet.guard_player_dy, bullet.guard_player_dx)

            # Calculate and add the bullet velocity to each specific bullet's position in the list
            bullet.new_velocity = (warden_bullets[n].speed * cos(bullet.angle), warden_bullets[n].speed * sin(bullet.angle))
            warden_bullets[n].velocity = bullet.new_velocity

    def shoot(self):

        if len(warden_shots) <= 8:  # If warden has shot less than 8 times
            now = pygame.time.get_ticks()
            if now - self.last >= 1500:  # Wait 1.5 seconds
                self.last = now
                self.start_shoot()  # Shoot again

        if len(warden_shots) > 8:  # If warden has shot 8 or more times

            now = pygame.time.get_ticks()
            if now - self.last >= 4000:  # Wait 4 seconds
                self.last = now
                del warden_shots[:]  # Empty the list that keeps track of how many time the warden has shot

    def start_shoot(self):  # Function that shoots each bullet

        if self.left:  # If guard is looking left
            warden_bullets.append(Bullet(self.x, self.y + 75))
            self.bullet_velocity(0, 75)
            warden_shots.append([])

        if self.right:  # If guard is looking right
            warden_bullets.append(Bullet(self.x + 57, self.y + 7))
            self.bullet_velocity(57, 7)
            warden_shots.append([])

        if self.up:  # If guard is looking up
            warden_bullets.append(Bullet(self.x + 7, self.y))
            self.bullet_velocity(7, 0)
            warden_shots.append([])

        if self.down:  # If guard is looking down

            warden_bullets.append(Bullet(self.x + 75, self.y + 57))
            self.bullet_velocity(75, 57)
            warden_shots.append([])

        else:
            pass

    def bullet_change(self):  # Function that updates each bullet's position with the velocity calculated

        for bullet in warden_bullets:  # For each bullet

            # Bullet interaction with player's hitbox
            if bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > \
                    player.hitbox[1]:
                if bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox[0] + \
                        player.hitbox[2]:
                    player.shot()

                    # If player's health is 0, print a game over message to the screen and end the game
                    if player.health == 0:
                        pass
                        message_to_screen("You lost", red, player.x, player.y, size="medium")
                        pygame.display.update()
                        pygame.quit()

                    # Pop/delete the bullet after it hits a player
                    warden_bullets.pop(warden_bullets.index(bullet))

            if screen_width > bullet.x > 0:

                n = 0
                while n <= len(warden_bullets) - 1:
                    # For each bullet, constantly change its x and y position as determined by the calculated velocity
                    warden_bullets[n].x += warden_bullets[n].velocity[0]
                    warden_bullets[n].y += warden_bullets[n].velocity[1]
                    n += 1

                # If the bullet leaves the screen, pop the bullet
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


class Projectile:  # Class that defines each projectile
    def __init__(self, x, y):
        self.x = x  # Projectile x position
        self.y = y  # Projectile y position

    def draw(self):  # Function that draws each projectile to the screen
        pygame.draw.circle(win, self.color, (int(round(self.x, 0)), int(round(self.y, 0))), self.radius)


class Bullet(Projectile):  # Class that defines the bullet projectile
    def __init__(self, x, y):
        super().__init__(x, y)  # Calling __init__ from class Projectile

        self.velocity = 0  # Bullet velocity
        self.radius = 3  # Bullet radius
        self.color = black  # Bullet color
        self.speed = 15  # Bullet speed


def guardsKilled():  # Function that shows how many enemy players have been killed on the screen
    if weapon == 1:
        message_to_screen("Bullets left: "  + str(stock[0]), red, 1090, 580, "small")
    else:
        if stock[0] >=0:
            message_to_screen("Bullets left: " + str(stock[0]) + "/" + str(ammoleft), red, 1090, 580, "small")
        if stock[0] <= 0:
            message_to_screen("Bullets left: 0/" + str(ammoleft), red, 1090, 580, "small")
    if level_list[0] == 1:  # Guards
        message_to_screen("Guards Killed: " + str(len(guards_killed)) + "/7", red, 1090, 20, "small")

    if level_list[0] == 4:  # Towers
        message_to_screen("Guards Towers Killed: " + str(len(guardTowersKilled)) + "/2", red, 1050, 20, "small")

    if level_list[0] == 5:  # Wardens
        message_to_screen("Wardens Killed: " + str(len(wardens_killed)) + "/1", red, 1060, 20, "small")


player = Player(200, 255, 83, 55, 'player', 10)  # Defining the player by using the Player class

level_list = [1, 0]  # Creating a list that is used to indicate which level the player is on

if level_list[0] == 1:  # If level 1
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(-1)
    level_list[1] = pygame.image.load("level_1.png")  # Level image sent to list

player_gold = [0]


def redraw():  # Function used to draw to the screen

    if level_list[0] == 1: # and len(guards_killed) >= 6:  # If player is on the first level and has cleared all of the enemies
        if player.x == 1100:  # If player reaches the right side of the screen, send him back to the left side
            player.x = 75
            player.y = 255

            level_list[0] += 1  # Increase the level number
            level_list[1] = pygame.image.load("level_" + str(level_list[0]) + ".png")  # Level image sent to list

            # Start the player looking right
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        else:
            pass

    if level_list[0] == 2:  # If player is on the first level and has cleared all of the enemies
        if player.x == 950:  # If player reaches the right side of the screen, send him back to the left side
            player.x = 75
            player.y = 255

            level_list[0] += 1  # Increase the level number
            level_list[1] = pygame.image.load("level_" + str(level_list[0]) + ".png")  # Level image sent to list

            # Start the player looking right
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        else:
            pass

    if level_list[0] == 3:  # If player is on the first level and has cleared all of the enemies
        shop()

    if level_list[0] == 4 and len(guardTowersKilled) >= 2:  # If player is on the second level and has cleared all of the enemies

        if player.x == 900:  # If player reaches the right side of the screen, send him back to the left side
            player.x = 75
            player.y = 255

            level_list[0] += 1  # Increase the level number
            level_list[1] = pygame.image.load("level_" + str(level_list[0]) + ".png")  # Level image sent to list

            # Start the player looking right
            player.left = False
            player.right = True
            player.down = False
            player.up = False

    if level_list[0] == 5 and len(wardens_killed) >= 1:  # If player is on the third level and has cleared all of the enemies

        if player.x == 900:  # If player reaches the right side of the screen, send him back to the left side
            player.x = 75
            player.y = 255

            level_list[0] += 1  # Increase the level number
            level_list[1] = pygame.image.load("level_" + str(level_list[0]) + ".png")  # Level image sent to list

            # Start the player looking right
            player.left = False
            player.right = True
            player.down = False
            player.up = False

    if level_list[0] == 6:  # If the player is on the fourth level

        if player.x == 600:  # If the player reaches the finish line (helicopter)
            # Show "You Win" text on the screen
            message_to_screen("You won", green, player.x, player.y, size="medium")
            pygame.display.update()

            # Wait 3 seconds then close the game
            time.sleep(3)
            pygame.quit()

    win.blit(level_list[1], (0, 0))  # Show the current level image on the screen
    if level_list[0] != 3:
        player.draw()  # Draw the player to the screen
        for i in player_bullets:  # For each of the player's bullets
            i.draw()  # Draw each bullet to the screen


    message_to_screen("Coins: " + str(player_gold[0]), red, 900, 20, "small")
    guardsKilled()  # Function that shows how many enemies the player has killed on the top right of the screen
    for guard in guards:  # For each guard
        if len(guards_killed) <= 6 and level_list[0] == 1:  # Insure that the player has yet to clear all of the enemies on the 1st level
            guard.chase()  # Guard chases player
            guard.draw()  # Guard's image is drawn to the screen
            guard.shoot()  # Guard shoots
            guard.bullet_change()  # Bullet changes direction to follow the path to the player

        else:
            pass

    for bullet in guard_bullets:  # For each of the guard's bullets
        bullet.draw()  # Draw the bullet to the screen

    for tower in guardTowers:  # For each guard tower
        if len(guardTowersKilled) <= 1 and level_list[0] == 4:  # Insure that the player has yet to clear all of the enemies on the 2nd level
            tower.draw()  # Tower's health bar is drawn to the screen
            tower.shoot()  # Tower shoots
            tower.bullet_change()  # Bullet changes direction to follow the path to the player
        else:
            pass

    for bullet in guardTowerBullets:  # For each of the tower's bullets
        bullet.draw()  # Draw the bullet to the screen

    for warden in wardens:  # For each warden
        if len(wardens_killed) <= 0 and level_list[0] == 5:  # Insure that the player has yet to clear all of the enemies on the 3rd level
            warden.chase()  # Warden chases player
            warden.draw()  # Warden's image is drawn to the screen
            warden.shoot()  # Warden shoots
            warden.bullet_change()  # Bullet changes direction to follow the path to the player

        else:
            pass

    for bullet in warden_bullets:  # For each of the warden's bullets
        bullet.draw()  # Draw the bullet to the screen

    pygame.display.update()  # Update the window screen


def levelRestrictions():  # Creating restrictions for each level/screen
    keys = pygame.key.get_pressed()
    # boundaries for level 1
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

        if keys[pygame.K_w] and player.y > 205:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 330:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False

    if level_list[0] == 2:
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

        if keys[pygame.K_w] and player.y > 205:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 330:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False

    if level_list[0] == 3:
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

        if keys[pygame.K_w] and player.y > 205:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 330:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False
    # boundaries for level 2
    if level_list[0] == 4:
        if keys[pygame.K_a] and player.x > 0 + 215:
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

        if keys[pygame.K_w] and player.y > 175:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 365:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False
    # boundaries for level 3
    if level_list[0] == 5:
        if keys[pygame.K_a] and player.x > 0 + 175:
            player.x -= player.speed
            player.left = True
            player.right = False
            player.down = False
            player.up = False

        if keys[pygame.K_d] and player.x < screen_width - player.height - 190:
            player.x += player.speed
            player.left = False
            player.right = True
            player.down = False
            player.up = False

        if keys[pygame.K_w] and player.y > 110:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 390:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False
    # boundaries for level 4
    if level_list[0] == 6:

        if keys[pygame.K_a] and player.x > 125:
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

        if keys[pygame.K_w] and player.y > 40:
            player.y -= player.speed
            player.left = False
            player.right = False
            player.down = False
            player.up = True

        if keys[pygame.K_s] and player.y < 0 + 500:
            player.y += player.speed
            player.left = False
            player.right = False
            player.down = True
            player.up = False


clock = pygame.time.Clock()  # Will be used to define the FPS (frames per second) of the game
run = True  # Determines whether the game is running

# Game intro screens


def game_loop():
    run = True
    while run:  # While the game is active/running. If run ever = False, end the game.
        global n

        keys = pygame.key.get_pressed()  # Variable that defines a key press

        for event in pygame.event.get():  # For each event in the game
            if event.type == pygame.QUIT:  # If game is closed with "X"
                run = False  # End the game

            if keys[pygame.K_r]:  # If the r key is pressed
                reloadsound.play()
                del shots[:]  # Clear the list that counts the number of shots made
                player.loaded = True  # Insures that the character is loaded to shoot
                global ammoleft
                if weapon == 1:
                    pass
                else:
                    if 1 <= ammoleft < 6:
                        if stock[0] + ammoleft <= 6:
                            stock[0] += ammoleft
                            ammoleft -= ammoleft
                        elif stock[0] + ammoleft > 6:
                            k = 6 - int(stock[0])
                            stock[0] += k
                            ammoleft -= k
                    elif ammoleft == 0:
                        stock[0] += 0
                        ammoleft -= 0
                    else:
                        k = 6 - int(stock[0])
                        stock[0] += k
                        ammoleft -= k

            if event.type == pygame.MOUSEBUTTONDOWN:  # If the mouse is clicked
                if len(player_bullets) < 6:  # If the number of bullets on the screen at any time is less than or equal to six

                    if len(shots) >= 6:  # If 6 bullets have been shot
                        player.loaded = False  # Gun is no longer loaded with enough bullets to shoot. The player must reload.

                        if weapon == 1:
                            player.loaded = True
                        else:
                            pass

                    player.bulletVelCalc()  # Function that starts moving the bullet toward the click's position

        if len(guards) == 0 and level_list[0] == 1:  # If the player is on level 1, start adding guards to the screen
            guards.append(Mob(1200, 255, 82, 61, 'Guard', 10))

        if len(guardTowers) == 0 and level_list[0] == 4:  # If the player is on level 2, start adding towers to the screen
            guardTowers.append(GuardTower(715, 555, 82, 61, 10))
            guardTowers.append(GuardTower(715, 60, 82, 61, 10))

        if len(wardens) == 0 and level_list[0] == 5:  # If the player is on level 3, start adding wardens to the screen
            wardens.append(Warden(980, 300, 82, 61, 'Guard', 10))

        g = 0  # Guards start at 0
        gt = 0  # 1st tower
        gt_2 = 1  # 2nd tower
        for bullet in player_bullets:  # For each bullet
            print(stock[0])
            if stock[0] >= 0:
                if level_list[0] == 1:  # If the player is on the first level
                    try:
                        # Bullet interaction with guards
                        if bullet.y - bullet.radius < guards[g].hitbox[1] + guards[g].hitbox[3] and bullet.y + bullet.radius > \
                                guards[g].hitbox[1]:
                            if bullet.x + bullet.radius > guards[g].hitbox[0] and bullet.x - bullet.radius < guards[g].hitbox[0] + \
                                    guards[g].hitbox[2]:

                                guards[g].shot()  # Guard loses 1 health
                                for guard in guards:  # For each guard
                                    if guards[g].health == 0:  # If the guard has 0 health
                                        guards_killed.append([])  # Add to the number of guards killed
                                        player_gold[0] = player_gold[0] + 50
                                        guards.pop(guards.index(guard))  # Pop/delete the killed guard

                                player_bullets.pop(player_bullets.index(bullet))  # Delete the player's bullet from the screen
                    except IndexError:
                        pass

                if level_list[0] == 4:  # If the player is on the second level
                    try:
                        # Bullet interaction with 1st guard tower
                        if bullet.y - bullet.radius < guardTowers[gt].hitbox[1] + guardTowers[gt].hitbox[3] and bullet.y + bullet.radius > \
                                guardTowers[gt].hitbox[1]:
                            if bullet.x + bullet.radius > guardTowers[gt].hitbox[0] and bullet.x - bullet.radius < guardTowers[gt].hitbox[
                                0] + \
                                    guardTowers[gt].hitbox[2]:

                                guardTowers[gt].shot()  # Tower loses 1 health
                                if guardTowers[gt].health == 0:  # If the tower has 0 health
                                    guardTowersKilled.append([])  # Add to the number of towers killed
                                    guardTowers.pop(gt)  # Pop/delete the killed tower

                                player_bullets.pop(player_bullets.index(bullet))  # Delete the player's bullet from the screen

                        # Bullet interaction with 2nd guard tower
                        if bullet.y - bullet.radius < guardTowers[gt_2].hitbox[1] + guardTowers[gt_2].hitbox[3] and bullet.y + bullet.radius > \
                                guardTowers[gt_2].hitbox[1]:
                            if bullet.x + bullet.radius > guardTowers[gt_2].hitbox[0] and bullet.x - bullet.radius < guardTowers[gt_2].hitbox[
                                0] + \
                                    guardTowers[gt_2].hitbox[2]:

                                guardTowers[gt_2].shot()  # Tower loses 1 health
                                if guardTowers[gt_2].health == 0:  # If the tower has 0 health
                                    guardTowersKilled.append([])  # Add to the number of towers killed
                                    guardTowers.pop(gt_2)  # Pop/delete the killed tower

                                player_bullets.pop(player_bullets.index(bullet))  # Delete the player's bullet from the screen

                    except IndexError:
                        pass

                if level_list[0] == 5:  # If the player is on the third level
                    try:

                        # Bullet interaction with the warden
                        if bullet.y - bullet.radius < wardens[g].hitbox[1] + wardens[g].hitbox[3] and bullet.y + bullet.radius > \
                                wardens[g].hitbox[1]:
                            if bullet.x + bullet.radius > wardens[g].hitbox[0] and bullet.x - bullet.radius < wardens[g].hitbox[0] + \
                                    wardens[g].hitbox[2]:

                                wardens[g].shot()  # Warden loses 1 health
                                for warden in wardens:  # For each warden
                                    if wardens[g].health == 0:  # If the warden has 0 health
                                        wardens_killed.append([])  # Add to the number of wardens killed
                                        wardens.pop(wardens.index(warden))  # Pop/delete the killed warden

                                player_bullets.pop(player_bullets.index(bullet))  # Delete the player's bullet from the screen
                    except IndexError:
                        pass

                # Delete the player's bullet if it leaves the screen
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

        levelRestrictions()  # Call the screen restriction for the level
        redraw()  # Call the redraw function to update the screen
        clock.tick(60)  # 60 FPS

game_intro()
pygame.quit()  # End the game
