import pygame

pygame.init()

display_width = 1000
display_height = 500

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Limbo')

clock = pygame.time.Clock()

x_change = 0
y_change = 0


class PlayerImage:
    def __init__(self, x, y, scale_x, scale_y, image):
        self.x = x
        self.y = y
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.scale_x, self.scale_y))

        gameDisplay.blit(self.image, (self.x, self.y))


player = PlayerImage(0, 0, 300, 300, 'prisoner.png')


crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

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
        gameDisplay.blit(player.image, (player.x, player.y))

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

