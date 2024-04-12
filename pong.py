import pygame, sys, random

def draw_mov_obj():
    # moving objects
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
def static_background():
    # static background graphic
    screen.fill(background_color)

    # draws match field lines
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.ellipse(screen, light_grey, [screen_width / 2 - 110, screen_height / 2 - 110, 220, 220], 2)

def dynamic_background():
    # creates labels for scores
    score_player_label = main_font.render(f"Score Player: {score_player}", 1, light_grey)
    score_opponent_label = main_font.render(f"Score Opponent: {score_opponent}", 1, light_grey)

    screen.blit(score_player_label, (screen_width - 150, 0 + 15))
    screen.blit(score_opponent_label, (0 + 50, 0 + 15))

    # creates labels for lives
    lives_player_label = main_font.render(f"Lives: {player_lives}", 1, light_grey)
    lives_opponent_label = main_font.render(f"Lives: {opponent_lives}", 1, light_grey)

    screen.blit(lives_player_label, (screen_width - 150, 0 + 35))
    screen.blit(lives_opponent_label, (0 + 50, 0 + 35))

    timer_label = timer_font.render(f"Timer: {game_time_sec} sec", 1, light_grey)

    screen.blit(timer_label, (screen_width / 2 - 70, 0 + 20))

def count_score_player():
    global score_player
    score_player += 1

def count_score_opponent():
    global score_opponent
    score_opponent += 1

def count_player_lives():
    global player_lives
    player_lives -= 1

def count_opponent_lives():
    global opponent_lives
    opponent_lives -= 1


def ball_animation():
    global ball_speed_x, ball_speed_y, score_opponent, score_player
    # moves from the start
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # bouncing ball animation
    if ball.left <= - 45:
        ball_restart()
        count_opponent_lives()
    if ball.right >= screen_width + 45:
        ball_restart()
        count_player_lives()

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # collisions with players rectangles
    if ball.colliderect(player):
        ball_speed_x *= -1
        count_score_player()

    if ball.colliderect(opponent):
        ball_speed_x *= -1
        count_score_opponent()

def opponent_movement():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1, -1))

pygame.init()
pygame.font.init()

timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 1000)

clock = pygame.time.Clock()
game_time_sec = 60

main_font = pygame.font.SysFont("Bahnschrift", 15, bold=False)
timer_font = pygame.font.SysFont("Bahnschrift", 25, bold=False)

screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Pong')

running = True

ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)
player = pygame.Rect(screen_width - 25, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(15, screen_height/2 - 70, 10, 140)

score_player = 0
score_opponent = 0
player_lives = 5
opponent_lives = 5

background_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

player_speed = 0
opponent_speed = 7
def main():
    global screen_width, screen_height
    global player_speed, game_time_sec

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

            if event.type == timer_event:
                game_time_sec -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 7
                if event.key == pygame.K_UP:
                    player_speed += 7

        # draws objects
        static_background()
        dynamic_background()
        draw_mov_obj()

        # creates movements
        ball_animation()
        opponent_movement()
        player_animation()

        if player_lives < 0 or game_time_sec < 0:
            game_over_menu()


        pygame.display.flip()

        clock.tick(60)

def game_over_menu():
    title_font = pygame.font.SysFont("Bahnschrift", 45, bold=False)
    end_font = pygame.font.SysFont("Bahnschrift", 25, bold=False)
    run = True
    while run:
        static_background()

        begin_label = title_font.render("Game Over!", 1, (255, 255, 255))
        screen.blit(begin_label, (screen_width / 2 - begin_label.get_width() / 2, screen_height / 2 - 190))

        begin_label = end_font.render("You've lost.", 1, (255, 255, 255))
        screen.blit(begin_label, (screen_width / 2 - begin_label.get_width() / 2, screen_height / 2 - 140))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



def main_menu():
    title_font = pygame.font.SysFont("Bahnschrift", 45, bold=False)
    begin_font = pygame.font.SysFont("Bahnschrift", 25, bold=False)
    run = True
    while run:
        static_background()

        begin_label = title_font.render("Welcome to the Pong Game!", 1, (255, 255, 255))
        screen.blit(begin_label, (screen_width / 2 - begin_label.get_width() / 2, screen_height / 2 - 270))

        begin_label = begin_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        screen.blit(begin_label, (screen_width / 2 - begin_label.get_width() / 2, screen_height / 2 - 180))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()
main_menu()