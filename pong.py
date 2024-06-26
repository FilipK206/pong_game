import math
import pygame
import sys
import random

# Function to draw moving objects
def draw_mov_obj():
    # Draw player, opponent, and ball
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)

# Function to draw static background
def static_background():
    # Fill the screen with background color
    screen.fill(background_color)

    # Draw match field lines and center circle
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.ellipse(screen, light_grey, [screen_width / 2 - 110, screen_height / 2 - 110, 220, 220], 2)

# Function to draw dynamic elements of the background (scores, lives, timer)
def dynamic_background():
    # Render and blit score labels
    score_player_label = main_font.render(f"Score Player: {score_player}", 1, light_grey)
    score_opponent_label = main_font.render(f"Score Opponent: {score_opponent}", 1, light_grey)

    screen.blit(score_player_label, (screen_width - 150, 0 + 15))
    screen.blit(score_opponent_label, (0 + 50, 0 + 15))

    # Render and blit life labels
    lives_player_label = main_font.render(f"Lives: {player_lives}", 1, light_grey)
    lives_opponent_label = main_font.render(f"Lives: {opponent_lives}", 1, light_grey)

    screen.blit(lives_player_label, (screen_width - 150, 0 + 35))
    screen.blit(lives_opponent_label, (0 + 50, 0 + 35))

    # Render and blit timer label
    timer_label = timer_font.render(f"Timer: {game_time_sec} sec", 1, light_grey)
    screen.blit(timer_label, (screen_width / 2 - 70, 0 + 20))

# Function to update player's score
def count_score_player():
    global score_player
    score_player += 1

# Function to update opponent's score
def count_score_opponent():
    global score_opponent
    score_opponent += 1

# Function to decrease player's lives
def count_player_lives():
    global player_lives
    player_lives -= 1

# Function to decrease opponent's lives
def count_opponent_lives():
    global opponent_lives
    opponent_lives -= 1

def reflect_ball(ball, paddle):
    global ball_speed_x, ball_speed

    # Calculate the position of collision on the paddle
    paddle_collision_point = ball.y + ball.height / 2 - (paddle.y + paddle.height / 2)

    # Normalize the collision point to the range [-1, 1]
    normalized_collision_point = paddle_collision_point / (paddle.height / 2)

    # Calculate the reflection angle based on the normalized collision point
    reflection_angle = normalized_collision_point * (math.pi / 4)  # Max bounce angle: 45 degrees

    # Reverse the horizontal velocity and adjust the vertical velocity based on the reflection angle
    ball_speed_x = -abs(ball_speed_x)
    ball_speed_y = ball_speed * math.sin(reflection_angle)

    return ball_speed_x, ball_speed_y

# Function to animate the ball
def ball_animation():
    global ball_speed_x, ball_speed_y
    global score_opponent, score_player

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.left <= - 45:
        ball_restart()
        count_opponent_lives()
    if ball.right >= screen_width + 45:
        ball_restart()
        count_player_lives()
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Ball collision with players
    if ball.colliderect(player):
        ball_speed_x, ball_speed_y = reflect_ball(ball, player)
        count_score_player()

    if ball.colliderect(opponent):
        ball_speed_x, ball_speed_y = reflect_ball(ball, opponent)
        ball_speed_x *= -1
        ball_speed_y *= -1
        count_score_opponent()

# Function to move the opponent paddle
def opponent_movement():
    # Calculate the target position for the opponent paddle
    target_y = ball.y + ball.height / 2

    # Adjust opponent paddle's position towards the target
    if opponent.centery < target_y:
        opponent.centery += min(opponent_speed, target_y - opponent.centery)
    elif opponent.centery > target_y:
        opponent.centery -= min(opponent_speed, opponent.centery - target_y)

    if opponent.top <= 0:
        opponent.top = 0

    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

# Function to move the player paddle
def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height

# Function to reset the ball position and speed
def ball_restart():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1, -1))

# Initialize Pygame
pygame.init()
pygame.font.init()

# Set up timer event
timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 1000)

# Set up clock
clock = pygame.time.Clock()
game_time_sec = 60

# Set up fonts
main_font = pygame.font.SysFont("Bahnschrift", 15, bold=False)
timer_font = pygame.font.SysFont("Bahnschrift", 25, bold=False)

# Set up screen dimensions
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up window title
pygame.display.set_caption('Pong')

# Initialize game variables
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

ball_speed = 8
ball_speed_x = ball_speed * random.choice((1, -1))
ball_speed_y = ball_speed * random.choice((1, -1))

paddle_speed = 9
player_speed = 0
opponent_speed = paddle_speed

# Main game loop
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
                    player_speed += paddle_speed
                if event.key == pygame.K_UP:
                    player_speed -= paddle_speed

            if event.type == timer_event:
                game_time_sec -= 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= paddle_speed
                if event.key == pygame.K_UP:
                    player_speed += paddle_speed

        # Draw background and objects
        static_background()
        dynamic_background()
        draw_mov_obj()

        # Move objects
        ball_animation()
        opponent_movement()
        player_animation()

        # Check for game over or win conditions
        if player_lives < 0:
            result_menu("You have lost.", "Try next time to be better.")

        if opponent_lives < 0 or (game_time_sec < 0 and score_player > score_opponent):
            result_menu("You have won!", "You are the best!")
        elif game_time_sec < 0 and score_player < score_opponent:
            result_menu("You have lost.", "Try next time to be better.")
        elif game_time_sec < 0 and score_player < score_opponent:
            result_menu("It is a draw.", "Try next time to be better.")

        # Update display and limit FPS
        pygame.display.flip()
        clock.tick(60)

# Function to display results
def result_menu(title_result, text_result, padding=50):
    title_font = pygame.font.SysFont("Bahnschrift", 45, bold=False)
    end_font = pygame.font.SysFont("Bahnschrift", 25, bold=False)
    run = True
    while run:
        screen.fill(background_color)

        begin_label = title_font.render(title_result, 1, (255, 255, 255))
        screen.blit(begin_label, (screen_width / 2 - begin_label.get_width() / 2, screen_height / 2 - (2*padding)))

        begin_label = end_font.render(text_result, 1, (255, 255, 255))
        screen.blit(begin_label, (screen_width / 2 - begin_label.get_width() / 2, screen_height / 2 - padding))

        begin_label = end_font.render(f"Your score: {score_player}", 1, (255, 255, 255))
        screen.blit(begin_label, (screen_width / 2 - begin_label.get_width() / 2, screen_height / 2))

        begin_label = end_font.render(f"Your opponent score: {score_opponent}", 1,(255, 255, 255))
        screen.blit(begin_label, (screen_width / 2 - begin_label.get_width() / 2, screen_height / 2 + padding))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


# Function to display main menu
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

# Start the game by displaying the main menu
main_menu()
