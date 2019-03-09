import pygame

pygame.init()

clock = pygame.time.Clock()


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Limbo')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


all_sprites = pygame.sprite.Group()

# Update
all_sprites.update()

# Draw / render

all_sprites.draw(screen)


class SpriteSheet(object):  # Loading sprite sheets

    def __init__(self, file_name, width, height, range_count, frame, row):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.cells = []
        self.width, self.height = width, height
        self.frame = frame

        for sprite in range(range_count):
            rect = pygame.Rect(frame * width, row * height, width, height)
            image = pygame.Surface(rect.size).convert()
            image.blit(self.sprite_sheet, (0, 0), rect)
            image.set_colorkey(BLACK)
            self.cells.append(image)

        self.img = self.cells[self.frame]
        self.character_rect = self.img.get_rect()
        self.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


guard = SpriteSheet('GregTest.png', 80, 72, 3, 1, 0)

game_exit = False


def crash():
    global game_exit
    game_exit = True


def game_loop():

    while not game_exit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                crash()

        screen.fill(WHITE)

        screen.blit(guard.img, (0, 0))
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
