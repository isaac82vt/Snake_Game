import pygame
import sys
import random

# initialize game engine
pygame.init()

# set up game window size and title
SCREEN_SIZE = (450, 450)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Snake Game")

# set up game colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# initialize clock to control game speed
clock = pygame.time.Clock()

# set up snake starting position and size
snake_x = 150
snake_y = 150
snake_size = 10
snake_list = []
snake_length = 1

# set up food position and size
food_x = round(random.randrange(0, SCREEN_SIZE[0]-10)/10.0)*10.0
food_y = round(random.randrange(0, SCREEN_SIZE[1]-10)/10.0)*10.0
food_size = 10

# set up font for displaying score
font = pygame.font.Font(None, 30)

# set up initial direction and speed
direction = "right"
speed = 10

# set up initial score
score = 0

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # change direction based on key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            if event.key == pygame.K_DOWN:
                direction = "down"
            if event.key == pygame.K_LEFT:
                direction = "left"
            if event.key == pygame.K_RIGHT:
                direction = "right"

    # move snake based on direction
    if direction == "right":
        snake_x += speed
    elif direction == "left":
        snake_x -= speed
    elif direction == "up":
        snake_y -= speed
    elif direction == "down":
        snake_y += speed

    # add new position to snake list
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    # remove old positions if snake has grown
    if len(snake_list) > snake_length:
        del snake_list[0]

    # check if snake has collided with food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, SCREEN_SIZE[0]-10)/10.0)*10.0
        food_y = round(random.randrange(0, SCREEN_SIZE[1]-10)/10.0)*10.0
        snake_length += 1
        score += 10

        # check if snake has collided with edges
    if snake_x >= SCREEN_SIZE[0] or snake_x < 0 or snake_y >= SCREEN_SIZE[1] or snake_y < 0:
        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, [150, 225])
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    # check if snake has collided with itself
    for block in snake_list[:-1]:
        if block == snake_head:
            game_over_text = font.render("Game Over", True, WHITE)
            screen.blit(game_over_text, [150, 225])
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

    # clear screen and redraw food and snake
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, [food_x, food_y, food_size, food_size])
    for block in snake_list:
        pygame.draw.rect(screen, WHITE, [block[0], block[1], snake_size, snake_size])

    # display score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

    # update game display
    pygame.display.update()

    # set game speed
    clock.tick(10)

