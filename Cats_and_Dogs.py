import random
import pygame
from sys import exit

class Cloudz(pygame.sprite.Sprite):
    def __init__(self, cloud_image):
        super().__init__()
        self.image = pygame.image.load(cloud_image)
        speed = [-5, -4, -3, 3, 4, 5]  # speed array controls the speed at which the clouds move from side to side
        boundary = [-100, 480]  # the extreme left and right boudaries used to reset the clouds when they go off screen
        x_start = random.choice(boundary)
        y_start = random.randint(0, 320)
        self.rect = self.image.get_rect(topleft=(x_start, y_start))
        self.speed = random.choice(speed)

    def update(self):
        self.rect.x += self.speed
        if (self.rect.x < -100) or (self.rect.x > 480):
            speed = [-5, -4, -3, 3, 4, 5]
            boundary = [-100, 480]
            self.speed = random.choice(speed)
            self.rect.x = random.choice(boundary)
            self.rect.y = random.randint(0, 320)



pygame.init()

height = 640
width = 480
screen = pygame.display.set_mode((width, height))    # create window and set the width and height
pygame.display.set_caption("Cats_and_Dogs")             # set window name

# main background images
background = pygame.image.load("Resources/Background.png")
sky = pygame.image.load("Resources/Sky.png")
ground = pygame.image.load("Resources/Ground.png")


# Create sprite group for moving cloud objects
clouds = pygame.sprite.Group()
clouds.add(Cloudz("Resources/Cloud_One.png"))
clouds.add(Cloudz("Resources/Cloud_Two.png"))
clouds.add(Cloudz("Resources/Cloud_Three.png"))


while True:
    for event in pygame.event.get():     # Check all of the events within the pygame window.
        if event.type == pygame.QUIT:    # If any of the events are a "close_window" request:
            pygame.quit()                # The pygame operation will stop, and
            exit()                       # the exit (i.e. 'sys.exit()' ) function breaks the main loop allowing the
                                         # to end without errors.


    screen.blit(background, (0, 0))
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 500))
    clouds.draw(screen)
    clouds.update()

    pygame.display.update()   # update main window to draw the events for each cycle.
