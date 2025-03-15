import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15


BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (242, 235, 211)
CROSS_COLOR = (66, 66, 66)


CIRCLE = 1
CROSS = 2


CELL_SIZE = WIDTH // 3
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)


def draw_lines():
    """Draws the grid lines on the board."""
    
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)
    
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    """Draws the Xs and Os on the board."""
    for row in range(3):
        for col in range(3):
            if grid[row][col] == CIRCLE:
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 3, LINE_WIDTH)
            elif grid[row][col] == CROSS:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 4),
                                 (col * CELL_SIZE + 3 * CELL_SIZE // 4, row * CELL_SIZE + 3 * CELL_SIZE // 4),
                                 LINE_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * CELL_SIZE + 3 * CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 4),
                                 (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + 3 * CELL_SIZE // 4),
                                 LINE_WIDTH)


def check_winner():
    """Checks if a player has won."""
    
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] != 0:
            return grid[row][0]
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != 0:
            return grid[0][col]
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][2]
    return 0


def restart_game():
    """Restarts the game by clearing the grid."""
    global grid, player_turn
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player_turn = CROSS
    screen.fill(BG_COLOR)
    draw_lines()



player_turn = CROSS
game_over = False


draw_lines()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            
            mouseX, mouseY = event.pos
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE

            
            if grid[clicked_row][clicked_col] == 0:
                grid[clicked_row][clicked_col] = player_turn
                player_turn = CIRCLE if player_turn == CROSS else CROSS

                
                winner = check_winner()
                if winner != 0:
                    game_over = True
                    print(f"Player {winner} wins!")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False

    draw_figures()
    pygame.display.update()
