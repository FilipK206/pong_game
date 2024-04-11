import pygame, sys

pygame.init()

clock = pygame.time.Clock()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Pong')

running = True

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    pygame.draw()

    clock.tick(60)