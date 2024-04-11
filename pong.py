import pygame, sys

def ball_animation():
    global ball_speed_x, ball_speed_y
    # moves from the start
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # bouncing ball animation
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # collisions with players rectangles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


pygame.init()

clock = pygame.time.Clock()

screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Pong')

running = True

ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

background_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7

player_speed = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player.y += player_speed

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