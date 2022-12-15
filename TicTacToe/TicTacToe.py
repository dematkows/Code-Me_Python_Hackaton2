import numpy as np
import pygame
import sys

# initializes pygame
pygame.init()

# ----------------
#  CONSTANTS
# ----------------

width = 600
height = 600
line_width = 15
board_rows = 3
board_cols = 3
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55

red = (255, 0, 0)
bg_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('TIC TAC TOE')
screen.fill(bg_color)

# board
board = np.zeros((board_rows, board_cols))


# print(board)

def draw_lines():
    # 1st horizontal line
    pygame.draw.line(screen, line_color, (0, 200), (600, 200), line_width)
    # 2nd horizontal line
    pygame.draw.line(screen, line_color, (0, 400), (600, 400), line_width)
    # 1st vertical line
    pygame.draw.line(screen, line_color, (200, 0), (200, 600), line_width)
    # 2nd vertical line
    pygame.draw.line(screen, line_color, (400, 0), (400, 600), line_width)


def draw_figures():
    for row in range(board_rows):
        for column in range(board_cols):
            if board[row][column] == 1:
                pygame.draw.circle(screen, circle_color, (int(column * 200 + 100), int(row * 200 + 100)), circle_radius,
                                   circle_width)
            elif board[row][column] == 2:
                pygame.draw.line(screen, cross_color, (column * 200 + space, row * 200 + 200 - space),
                                 (column * 200 + 200 - space, row * 200 + space), cross_width)
                pygame.draw.line(screen, cross_color, (column * 200 + space, row * 200 + space),
                                 (column * 200 + 200 - space, row * 200 + 200 - space), cross_width)


def mark_square(row, column, player):
    board[row][column] = player


def available_square(row, column):
    return board[row][column] == 0


def is_board_full():
    for row in range(board_rows):
        for column in range(board_cols):
            if board[row][column] == 0:
                return False
    return True


def check_win(player):
    # vertical win check
    for column in range(board_cols):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            draw_vertical_winning_line(column, player)
            return True

    # horizontal win check
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_ascending_diagonal(player)
        return True

    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_descending_diagonal(player)
        return True

    return False


def draw_vertical_winning_line(column, player):
    posX = column * 200 + 100

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)


def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)


def draw_ascending_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)


def draw_descending_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)


def restart():
    screen.fill(bg_color)
    draw_lines()
    for row in range(board_rows):
        for column in range(board_cols):
            board[row][column] = 0


draw_lines()

player = 1

game_over = False

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // 200)
            clicked_column = int(mouseX // 200)

            if available_square(clicked_row, clicked_column):
                if player == 1:
                    mark_square(clicked_row, clicked_column, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_column, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()
