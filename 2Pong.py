import pygame
import random

# Initialize the font module from pygame
pygame.font.init()

# Window Dimensions
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Window caption
pygame.display.set_caption("2Pong")

# Colours
Baby_blue = (137, 207, 240)
Light_green = (0, 238, 0)
Orange = (255, 165, 0)
Red = (255, 0, 0)
Purple = (128, 0, 128)

# Player dimensions
PLAYER_WIDTH = 10
PLAYER_HEIGHT = 100
# Creating and placement of players
PLAYER1_RECT = pygame.Rect(20, HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
PLAYER2_RECT = pygame.Rect(WIDTH - 20 - PLAYER_WIDTH, HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
# Player Velocity
PLAYER_VEL = 7

# Time/Frame rate control
clock = pygame.time.Clock()

# Creating the ball
BALL_WIDTH = 15
BALL_HEIGHT = 15
BALL_RECT = pygame.Rect(WIDTH/2 - BALL_WIDTH/2, HEIGHT/2 - BALL_HEIGHT/2, BALL_WIDTH, BALL_HEIGHT)
# Ball velocity
BALL_x_VEL = 5
BALL_y_VEL = 5

# Generate random number for random ball start direction
random_start = random.randint(1,4)

PLAYER1_SCORE = 0
PLAYER2_SCORE = 0
FONT_TYPE = pygame.font.SysFont("franklingothicmedium", 20)

# Displaying to window
def draw():
    # Background colour
    WIN.fill(Baby_blue)
    PLAYER1_TEXT = FONT_TYPE.render(f"PLAYER 1: {PLAYER1_SCORE}", 1, Orange)
    PLAYER2_TEXT = FONT_TYPE.render(f"PLAYER 2: {PLAYER2_SCORE}", 1, Light_green)
    WIN.blit(PLAYER1_TEXT, (15,15))
    WIN.blit(PLAYER2_TEXT, (WIDTH - 10 - PLAYER2_TEXT.get_width(), 10))
    # Displaying players
    pygame.draw.rect(WIN, Orange, PLAYER1_RECT)
    pygame.draw.rect(WIN, Light_green, PLAYER2_RECT)
    # Displaying the ball
    pygame.draw.ellipse(WIN, Purple, BALL_RECT)
    # Update display
    pygame.display.update()

# Player movement
def player_movement():
    keys = pygame.key.get_pressed()
    # Player 1 movement
    if keys[pygame.K_w] and PLAYER1_RECT.y > 0:
        PLAYER1_RECT.y -= PLAYER_VEL
    elif keys[pygame.K_z] and PLAYER1_RECT.y <= HEIGHT - PLAYER_HEIGHT:
        PLAYER1_RECT.y += PLAYER_VEL
    # Player 2 movement
    if keys[pygame.K_UP] and PLAYER2_RECT.y > 0:
        PLAYER2_RECT.y -= PLAYER_VEL
    elif keys[pygame.K_DOWN] and PLAYER2_RECT.y <= HEIGHT - PLAYER_HEIGHT:
        PLAYER2_RECT.y += PLAYER_VEL

# Initial ball movement
def initial_ball_movement():
    if random_start == 1:
        BALL_RECT.x += BALL_x_VEL
        BALL_RECT.y += BALL_y_VEL
    elif random_start == 2:
        BALL_RECT.x -= BALL_x_VEL
        BALL_RECT.y -= BALL_y_VEL
    elif random_start == 3:
        BALL_RECT.x -= BALL_x_VEL
        BALL_RECT.y += BALL_y_VEL
    elif random_start == 4:
        BALL_RECT.x += BALL_x_VEL
        BALL_RECT.y -= BALL_y_VEL

# Main game function
def main():
    global BALL_x_VEL, BALL_y_VEL, PLAYER1_SCORE, PLAYER2_SCORE
    run = True

    # Main game loop
    while run:
        # Frame rate
        clock.tick(60)
        # Quit window functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        initial_ball_movement()
        # Ball collisions Top and Bottom
        if BALL_RECT.y <= 0:
            BALL_y_VEL = -BALL_y_VEL
        if BALL_RECT.y >= HEIGHT - BALL_HEIGHT:
            BALL_y_VEL = -BALL_y_VEL
        # Ball collisions with players
        if BALL_RECT.colliderect(PLAYER2_RECT) or BALL_RECT.colliderect(PLAYER1_RECT):
            BALL_x_VEL = -BALL_x_VEL

        player_movement()
        draw()

        # Losing collisions
        if BALL_RECT.x <= 0:
            PLAYER2_SCORE += 1
            # Pause game before quitting
            PLAYER2_WIN_TEXT = FONT_TYPE.render("PLAYER 2 WINS!", 1, Light_green)
            WIN.blit(PLAYER2_WIN_TEXT, (WIDTH/2 - PLAYER2_WIN_TEXT.get_width()/2, HEIGHT/2 - PLAYER2_WIN_TEXT.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            BALL_RECT.center = (WIDTH/2, HEIGHT/2)
            initial_ball_movement()
        elif BALL_RECT.x >= WIDTH - BALL_WIDTH:
            PLAYER1_SCORE += 1
            PLAYER1_WIN_TEXT = FONT_TYPE.render("PLAYER 1 WINS!", 1, Orange)
            WIN.blit(PLAYER1_WIN_TEXT,(WIDTH / 2 - PLAYER1_WIN_TEXT.get_width() / 2, HEIGHT / 2 - PLAYER1_WIN_TEXT.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(4000)
            BALL_RECT.center = (WIDTH / 2, HEIGHT / 2)
            initial_ball_movement()

    # Terminate game
    pygame.quit()


# Run as main file only
if __name__ == "__main__":
    main()
