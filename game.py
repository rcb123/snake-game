import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Snake')

# Set the dimensions of the snake
snake_block = 10

# Set the font for the score
font_style = pygame.font.SysFont("bahnschrift", 25)

# Set the score to 0
score = 0

# Set the coordinates for the snake
snake_position = [100, 50]

# Create the snake body
# Initialize an empty list for the snake body
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the food position
food_position = [random.randrange(1, (window_size[0] // snake_block)) * snake_block,
                 random.randrange(1, (window_size[1] // snake_block)) * snake_block]
food_spawn = True

# Set the direction of the snake
direction = "RIGHT"
change_to = direction

# Set the clock for the game
clock = pygame.time.Clock()

# Set the colors
# Set the color for the snake
snake_color = (255, 255, 255)

# Set the color for the food
food_color = (255, 0, 0)

# Set the color for the score
score_color = (255, 255, 255)

# Set the color for the background
bg_color = (0, 0, 0)


# Create a function to display the score on the screen
def show_score(choice, color, font, size, x, y):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (x, y)
    screen.blit(score_surface, score_rect)


# Create a function to end the game
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, score_color)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_size[0] / 2, window_size[1] / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()


# Create a function to check if the snake has collided with the boundaries of the window
def collision_with_boundaries(snake_head):
    if snake_head[0] >= window_size[0] or snake_head[0] < 0:
        game_over()
    if snake_head[1] >= window_size[1] or snake_head[1] < 0:
        game_over()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Validate the direction
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Update the position of the snake
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_position = [random.randrange(1, (window_size[0] // snake_block)) * snake_block,
                         random.randrange(1, (window_size[1] // snake_block)) * snake_block]
    food_spawn = True

    screen.fill(bg_color)

    for pos in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(pos[0], pos[1], snake_block, snake_block))

    pygame.draw.rect(screen, food_color, pygame.Rect(food_position[0], food_position[1], snake_block, snake_block))

    # Check if the snake has collided with the boundaries
    if snake_position[0] > window_size[0] or snake_position[0] < 0:
        game_over()
    if snake_position[1] > window_size[1] or snake_position[1] < 0:
        game_over()

    # Check if the snake has collided with itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, score_color, 'times new roman', 20, window_size[0] - 10, 10)

    # Refresh the screen
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)
