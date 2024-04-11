import pygame, sys

pygame.init()

clock = pygame.time.Clock()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Pong')

running = True

ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

background_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # static background graphic
    screen.fill(background_color)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.ellipse(screen, light_grey, [screen_width / 2 - 110, screen_height / 2 - 110, 220, 220], 2)

    # moving objects
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    
    pygame.display.flip()

    clock.tick(60)