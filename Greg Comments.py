import pygame
from math import atan2, sin, cos

pygame.init()

# Defining colours with hexadecimal values
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Loading them image for the background
level_1 = pygame.image.load('Level_1.png')

# Defining variables for screen width and height
screen_width = 1200
screen_height = 600

# Using Pygame to create the window in which the game will be played in
win = pygame.display.set_mode((screen_width, screen_height))

# Setting the caption name for the game
pygame.display.set_caption("Limbo")

# Class that difines all players
class Character:
    def __init__(self, x, y, width, height, name):

        self.name = name  # Name of character
        self.x = x  # starting x position of the character
        self.y = y  # starting y position of the character
        self.width = width  # width of character
        self.height = height  # height of character
        self.speed = 5  # speed at which the character will move at

        # starting directions
        self.left = False
        self.right = False
        self.down = False
        self.up = False

        # Loading images for each direction
        self.lookUp = [pygame.image.load(self.name + '90.png')]
        self.lookDown = [pygame.image.load(self.name + '270.png')]
        self.lookLeft = [pygame.image.load(self.name + '180.png')]
        self.lookRight = [pygame.image.load(self.name + '0.png')]
        self.lookIdle = [pygame.image.load(self.name + '90.png')]

    def draw(self):

        # Drawing the character's direction to the screen
        if self.left:  # If direction is left
            win.blit(self.lookLeft[0], (self.x, self.y))

        elif self.right:  # If direction is right
            win.blit(self.lookRight[0], (self.x, self.y))

        elif self.down:  # If direction is down
            win.blit(self.lookDown[0], (self.x, self.y))

        elif self.up:  # If direction is up
            win.blit(self.lookUp[0], (self.x, self.y))

        else:  # If no direction has been assigned ("idle" direction)
            win.blit(self.lookIdle[0], (self.x, self.y))


class Mob(Character):  # Class that defines each mob (e.g. guards)
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health  # health of mob


class Player(Character):  # Class that defines the player
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health  # health of player


class Projectile:  # Class that defines each projectile (e.g. bullets) in the game
    def __init__(self, x, y, radius, colour):
        self.x = x  # starting x position of the projectile
        self.y = y  # starting y position of the projectile
        self.radius = radius  # radius of projectile
        self.colour = colour  # colour of projectile

    def draw(self):
        # Drawing the projectile to the screen
        pygame.draw.circle(win, self.colour, (int(round(self.x, 0)), int(round(self.y, 0))), self.radius)


class Bullet(Projectile):  # Class that defines the bullet projectiles
    def __init__(self, x, y, radius, colour, velocity):
        super().__init__(x, y, radius, colour)
        self.velocity = velocity  # starting velocity of the bullet
        self.speed = .5  # speed at which a bullet moves


class Click:  # Class that defines each click
    def __init__(self, mouse_pos):
        self.mouse_pos = mouse_pos  # defines the x and y positions of the mouse


clock = pygame.time.Clock()  # Will be used to define the FPS (frames per second) of the game
run = True  # Determines whether the game is running

guard = Mob(200, 200, 82, 49, 'GuardGun', 6)  # Creating a guard character, pulling from the GuardGun images
player = Player(200, 200, 40, 60, 'prisoner', 6)  # Creating a player character, pulling from the prisoner images
bullets = []  # List that will hold all of the bullets
clicks = []  # List that will hold all of the mouse positions
shots = []  # List that will keep track of the number of shots (for reloading gun)


def redrawGameWindow():  # Function used to draw to the screen
    win.fill(green)  # Draw a green background
    guard.draw()  # Draw the guard
    player.draw()  # Draw the player
    for i in bullets:  # For each bullet
        i.draw()  # Draw the bullet
    pygame.display.update()  # Update the screen


while run:  # while the game is active/running
    global n

    keys = pygame.key.get_pressed()  # variable that defines a key press

    for event in pygame.event.get():  # for each event in the game
        if event.type == pygame.QUIT:  # if game is closed with "X"
            run = False  # end the game

        if keys[pygame.K_r]:  # if the r key is pressed
            del shots[:]  # clear the list that counts the number of shots made
            loaded = True  # insures that the character is loaded to shoot

        if event.type == pygame.MOUSEBUTTONDOWN:  # If the mouse is clicked
            if len(bullets) <= 6:  # if the number of bullets on the screen at any time is less than or equal to six

                loaded = True  # gun is loaded

                if len(shots) == 6:  # if 6 bullets have been shot
                    loaded = False  # Gun is no longer loaded with enough bullets to shoot. The character must reload.

                # function that determines the velocity (speed + direction) of the bullet
                def bullet_velocity(change_x, change_y):
                    for bullet in bullets:  # for each bullet shot
                        speed = 25  # starting speed is 0.5
                        bullet.mouse_position = pygame.mouse.get_pos()  # find the mouse click's position

                        # find the distance between the bullet's position at time = 0 to the click's position
                        bullet.mouse_player_dx = bullet.mouse_position[0] - (guard.x + change_x)
                        bullet.mouse_player_dy = bullet.mouse_position[1] - (guard.y + change_y)

                        # calculate the angle between the initial position of the bullet and the click's position
                        bullet.angle = atan2(bullet.mouse_player_dy, bullet.mouse_player_dx)

                        # calculate the velocity of the bullet using the speed and direction (angle)
                        bullet.new_velocity = (speed * cos(bullet.angle), speed * sin(bullet.angle))

                        # change the initial velocity of the bullet to the final (calculated) velocity of the bullet
                        # this will show the bullet moving to the direction where the mouse was clicked
                        n = len(bullets) - 1
                        bullets[n].velocity = bullet.new_velocity


                # Calculating mouse position again, but this time to restrict where the player can shoot at
                mouse_positions = pygame.mouse.get_pos()
                pos_none = (0, 0)

                # Create a value in a list for each click, but with the position of (0,0). This value will be updated
                # later for each click
                clicks.append(Click(pos_none))

                if loaded:  # If the gun is loaded
                    for click in clicks:  # for each click
                        s = len(clicks) - 1
                        clicks[s] = mouse_positions  # change the (0,0) position to the mouse click's position

                        # In the prototype, the character shooting for Greg is the guard. This is changed to the player
                        # /prisoner in the final game. The only difference is the image of the character. All
                        # functionality remains identical.
                        if guard.left:  # if the character (guard) is looking left

                            # Creating the restriction box
                            if clicks[s][0] <= (player.x + player.height / 2 + player.width / 2) - 200:
                                if clicks[s][1] <= (player.y + player.height / 2 + player.width / 2) + 200:
                                    if clicks[s][1] >= (player.y + player.height / 2 + player.width / 2) - 200:
                                        bullets.append(Bullet(guard.x, guard.y + 75, 4, black, 0))  # Create the bullet
                                        bullet_velocity(0, 75)  # Give the bullet its velocity
                                        # Add an element to the shots list that determines if the gun is loaded
                                        shots.append([])
                                        break  # move onto next click after bullet is shot
                            break  # move onto next click if restrictions not met

                        if guard.right:  # if the character (guard) is looking right

                            # Creating the restriction box
                            if clicks[s][0] >= (player.x + player.height / 2 + player.width / 2) + 200:
                                if clicks[s][1] >= (player.y + player.height / 2 + player.width / 2) - 200:
                                    if clicks[s][1] <= (player.y + player.height / 2 + player.width / 2) + 20:
                                        bullets.append(Bullet(guard.x + 57, guard.y + 7, 4, black, 0))  # Create the bullet
                                        bullet_velocity(57, 7)  # Give the bullet its velocity
                                        # Add an element to the shots list that determines if the gun is loaded
                                        shots.append([])
                                        break  # move onto next click after bullet is shot
                            break  # move onto next click if restrictions not met

                        if guard.up:  # if the character (guard) is looking up

                            # Creating the restriction box
                            if clicks[s][1] <= (player.y + player.height / 2 + player.width / 2) - 200:
                                if clicks[s][0] >= (player.x + player.height / 2 + player.width / 2) - 200:
                                    if clicks[s][0] <= (player.x + player.height / 2 + player.width / 2) + 200:
                                        bullets.append(Bullet(guard.x + 7, guard.y, 4, black, 0))  # Create the bullet
                                        bullet_velocity(7, 0)  # Give the bullet its velocity
                                        # Add an element to the shots list that determines if the gun is loaded
                                        shots.append([])
                                        break  # move onto next click after bullet is shot
                            break  # move onto next click if restrictions not met

                        if guard.down:  # if the character (guard) is looking down

                            # Creating the restriction box
                            if clicks[s][1] >= player.y + 200:
                                if clicks[s][0] >= (player.x + player.height / 2 + player.width / 2) - 200:
                                    if clicks[s][0] <= (player.x + player.height / 2 + player.width / 2) + 200:
                                        bullets.append(Bullet(guard.x + 75, guard.y + 57, 4, black, 0))  # Create the bullet
                                        bullet_velocity(75, 57) # Give the bullet its velocity
                                        # Add an element to the shots list that determines if the gun is loaded
                                        shots.append([])
                                        break  # move onto next click after bullet is shot
                            break  # move onto next click if restrictions not met

                        if guard.lookIdle:  # if the character (guard) is in idle/starting position

                            # Creating the restriction box
                            if clicks[s][1] <= (player.y + player.height / 2 + player.width / 2) - 200:
                                if clicks[s][0] >= (player.x + player.height / 2 + player.width / 2) - 200:
                                    if clicks[s][0] <= (player.x + player.height / 2 + player.width / 2) + 200:
                                        bullets.append(Bullet(guard.x + 7, guard.y, 4, black, 0))  # Create the bullet
                                        bullet_velocity(7, 0)  # Give the bullet its velocity
                                        # Add an element to the shots list that determines if the gun is loaded
                                        shots.append([])
                                        break  # move onto next click after bullet is shot
                            break  # move onto next click if restrictions not met

    for bullet in bullets:  # for each bullet
        if screen_width > bullet.x > 0:  # check if the bullet is within the visible screen

            n = 0
            while n <= len(bullets) - 1:
                # for each bullet, constantly change its x and y position as determined by the calculated velocity
                bullets[n].x += bullets[n].velocity[0]  # x position
                bullets[n].y += bullets[n].velocity[1]  # y position
                n += 1

            # pop/kill/destroy bullet if it leaves the screen
            if screen_width < bullet.x or bullet.x < 0:
                bullets.pop(bullets.index(bullet))

            if screen_height < bullet.y or bullet.y < 0:
                # Error handling. The computer loses control of bullets if they are being shoot too fast.
                try:
                    bullets.pop(bullets.index(bullet))

                except ValueError:
                    pass

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
