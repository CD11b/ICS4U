import pygame

pygame.init()

display_width = 700
display_height = 550

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Limbo')

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

clock = pygame.time.Clock()
game_exit = False


class PlayerImage:
    def __init__(self, x, y, scale_x, scale_y, image):
        self.x = x
        self.y = y
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.scale_x, self.scale_y))

        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def display(self):
        gameDisplay.blit(self.image, (self.x, self.y))


player = PlayerImage(5, 5, 150, 150, 'prisoner.png')


def crash():
    global game_exit

    game_exit = True


def game_loop():

    x_change = 0
    y_change = 0

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            player.x += x_change
            player.y += y_change

            gameDisplay.fill(green)

            player.display()

            if player.x > display_width - player.scale_x or player.x < 0:
                crash()
            if player.y > display_height - player.scale_y or player.y < 0:
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()

