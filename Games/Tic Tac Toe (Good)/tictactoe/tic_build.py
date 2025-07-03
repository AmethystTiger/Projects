import pygame
from tictactoe.constants import *
from copy import deepcopy
from random import choice

def dynamic_button(win, x, y, w, h, active_color, passive_color, txt):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    font = pygame.font.Font('newfont.ttf', SIDE // 4)
    text = font.render(txt, True, BLACK)
    box = text.get_rect()
    box.center = (x + w // 2, y + h // 2)

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(win, active_color, (x, y, w, h))
        if click[0] == 1:
            win.blit(text, box)
            return True
    else:
        pygame.draw.rect(win, passive_color, (x, y, w, h))

    win.blit(text, box)
def isWinner(board, letter):
    if board[0][0] == letter and board[0][1] == letter and board[0][2] == letter:
        return True
    if board[1][0] == letter and board[1][1] == letter and board[1][2] == letter:
        return True
    if board[2][0] == letter and board[2][1] == letter and board[2][2] == letter:
        return True

    if board[0][0] == letter and board[1][0] == letter and board[2][0] == letter:
        return True
    if board[0][1] == letter and board[1][1] == letter and board[2][1] == letter:
        return True
    if board[0][2] == letter and board[1][2] == letter and board[2][2] == letter:
        return True

    if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        return True
    if board[0][2] == letter and board[1][1] == letter and board[2][0] == letter:
        return True
    return False

class Build:

    def __init__(self, window):
        self.window = window
        self.player = 1
        self.grid = [['', '', ''],
                     ['', '', ''],
                     ['', '', '']]
        self.turn = 0

        self.click_able = True

        self.win = False
        self.lose = False

        self.x_win = 0
        self.o_win = 0
        self.x_scored = False
        self.o_scored = False

        self.main_menu = True

        self.is_AI = False

    def place(self, row , column):
        if self.click_able:
            if self.grid[row][column] == '' and self.player == 1:
                self.grid[row][column] = 'X'
            elif self.grid[row][column] == '' and self.player == 0:
                self.grid[row][column] = 'O'
    def show_main_menu(self):
        font = pygame.font.Font('newfont.ttf', 100)

        title1 = font.render("Welcome To", True, BLACK)
        title2 = font.render("Tic Tac Toe", True, BLACK)
        self.window.blit(title1, (5, 120))
        self.window.blit(title2, (5, 320))

        if dynamic_button(self.window, 600, 140, 375, 65, LIGHT_LIGHT_GREY, WHITE, "Player vs Computer"):
            self.main_menu = False
            self.is_AI = True
        if dynamic_button(self.window, 630, 340, 300, 65, LIGHT_LIGHT_GREY, WHITE, "Player vs Player"):
            self.main_menu = False
    def AI(self):
        # Default location
        default = (0, 0)

        # Creates a list of row, column locations that are not in use
        possible_moves = []
        for row in range(len(self.grid)):
            for col, letter in enumerate(self.grid[row]):
                if letter == '':
                    possible_moves.append((row, col))
        print(possible_moves)
        # Places O to win or to prevent a win
        for player in ['O', 'X']:
            for vector in possible_moves:
                grid_copy = deepcopy(self.grid)
                grid_copy[vector[0]][vector[1]] = player
                if isWinner(grid_copy, player):
                    return vector

        # Places O at a random corner
        corner_location = []
        for vector in possible_moves:
            if vector in ((0, 0), (0, 2), (2, 0), (2, 2)):
                corner_location.append(vector)
        if len(corner_location) > 0:
            return choice(corner_location)

        # Places O at the center
        if (1, 1) in possible_moves:
            default = (1, 1)
            return default

        # Places O at a random edge
        edge_location = []
        for vector in possible_moves:
            if vector in ((0, 1), (1, 0), (1, 2), (2, 1)):
                edge_location.append(vector)
        if len(edge_location) > 0:
            return choice(edge_location)

        # If game has ended
        return default

    def show_board(self):
        font = pygame.font.Font('newfont.ttf', SIDE)
        for row in range(ROWS):
            for column in range(COLUMNS):
                pygame.draw.rect(self.window, BLACK, (row * SIDE, column * SIDE, SIDE, SIDE), 4)
                text = font.render(self.grid[column][row], True, BLACK)
                box = text.get_rect()
                box.center = (row * SIDE + SIDE//2, column * SIDE + SIDE//2)
                self.window.blit(text, box)
    def check(self):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()

        # Calculate the current turn
        self.turn = 0
        for i in self.grid:
            for j in i:
                if j != "":
                    self.turn += 1

        # Calculate the current player
        if self.turn % 2 == 0:
            self.player = 1
        else:
            self.player = 0

        if self.is_AI and self.player == 0:
            p = self.AI()
            self.place(p[0], p[1])

        # Check for winner or loser
        if self.turn == 9:
            self.lose = True
        if self.turn > 4:
            self.check_for_X()
            self.check_for_O()
            self.final_screen()

        for row in range(ROWS):
            for column in range(COLUMNS):
                if row * SIDE < mouse[1] < row * SIDE + SIDE and column * SIDE < mouse[0] < column * SIDE + SIDE:
                    if click[0]:
                        self.place(row, column)
    def score(self):
        font = pygame.font.Font('newfont.ttf', SIDE * 3 // 10)

        # Draw top half of the score board
        pygame.draw.rect(self.window, BLACK, (BOARD_W, 0, SCORE_BREADTH, BOARD_H//2), 4)

        score_text = font.render("Score :", True, BLACK)
        x_text = font.render("X - ", True, BLACK)
        x_score = font.render(str(self.x_win), True, BLACK)
        o_text = font.render("O-", True, BLACK)
        o_score = font.render(str(self.o_win), True, BLACK)

        self.window.blit(score_text, (BOARD_W*1.013, BOARD_H*0.013))
        self.window.blit(x_text, (BOARD_W*1.013, BOARD_H*0.18))
        self.window.blit(x_score, (BOARD_W*1.15, BOARD_H*0.18))
        self.window.blit(o_text, (BOARD_W*1.013, BOARD_H*0.33))
        self.window.blit(o_score, (BOARD_W*1.15, BOARD_H*0.33))

        # Draw the bottom half of the score board
        pygame.draw.rect(self.window, BLACK, (BOARD_H, BOARD_H//2, SCORE_BREADTH, BOARD_H//2), 4)

        current_text = font.render("Current :", True, BLACK)
        current_player = font.render("X", True, BLACK)
        if self.player == 0:
            current_player = font.render("O", True, BLACK)
        reset_img = pygame.image.load("reset.png")

        self.window.blit(current_text, (BOARD_W * 1.013, BOARD_H * 0.513))
        self.window.blit(current_player, (BOARD_W * 1.35, BOARD_H * 0.513))
        if dynamic_button(self.window, ((SCREEN_W-BOARD_W)//2)+BOARD_W/1.04, BOARD_H * 0.87, SIDE//3, SIDE//3, LIGHT_GREY, WHITE, "R"):
            self.player = 1
            self.grid = [['', '', ''],
                         ['', '', ''],
                         ['', '', '']]
            self.turn = 0
            self.click_able = True
            self.o_scored = False
            self.x_scored = False
            self.win = False
            self.lose = False
            self.show_board()
        self.window.blit(reset_img, (((SCREEN_W-BOARD_W)//2)+BOARD_W/1.04, BOARD_H * 0.87))
    def main_game(self):
        if self.main_menu:
            self.show_main_menu()
        else:
            self.show_board()
            self.check()
            self.score()

    def check_for_X(self):
        if not self.x_scored:
            if self.grid[0][0] == 'X' and self.grid[0][1] == 'X' and self.grid[0][2] == 'X':
                self.x_win += 1
                self.x_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[1][0] == 'X' and self.grid[1][1] == 'X' and self.grid[1][2] == 'X':
                self.x_win += 1
                self.x_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[2][0] == 'X' and self.grid[2][1] == 'X' and self.grid[2][2] == 'X':
                self.x_win += 1
                self.x_scored = True
                self.win = True
                self.click_able = False

            elif self.grid[0][0] == 'X' and self.grid[1][0] == 'X' and self.grid[2][0] == 'X':
                self.x_win += 1
                self.x_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[0][1] == 'X' and self.grid[1][1] == 'X' and self.grid[2][1] == 'X':
                self.x_win += 1
                self.x_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[0][2] == 'X' and self.grid[1][2] == 'X' and self.grid[2][2] == 'X':
                self.x_win += 1
                self.x_scored = True
                self.win = True
                self.click_able = False

            elif self.grid[0][0] == 'X' and self.grid[1][1] == 'X' and self.grid[2][2] == 'X':
                self.x_win += 1
                self.x_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[0][2] == 'X' and self.grid[1][1] == 'X' and self.grid[2][0] == 'X':
                self.x_win += 1
                self.x_scored = True
                self.win = True
                self.click_able = False
    def check_for_O(self):
        if not self.o_scored:
            if self.grid[0][0] == 'O' and self.grid[0][1] == 'O' and self.grid[0][2] == 'O':
                self.o_win += 1
                self.o_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[1][0] == 'O' and self.grid[1][1] == 'O' and self.grid[1][2] == 'O':
                self.o_win += 1
                self.o_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[2][0] == 'O' and self.grid[2][1] == 'O' and self.grid[2][2] == 'O':
                self.o_win += 1
                self.o_scored = True
                self.win = True
                self.click_able = False

            elif self.grid[0][0] == 'O' and self.grid[1][0] == 'O' and self.grid[2][0] == 'O':
                self.o_win += 1
                self.o_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[0][1] == 'O' and self.grid[1][1] == 'O' and self.grid[2][1] == 'O':
                self.o_win += 1
                self.o_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[0][2] == 'O' and self.grid[1][2] == 'O' and self.grid[2][2] == 'O':
                self.o_win += 1
                self.o_scored = True
                self.win = True
                self.click_able = False

            elif self.grid[0][0] == 'O' and self.grid[1][1] == 'O' and self.grid[2][2] == 'O':
                self.o_win += 1
                self.o_scored = True
                self.win = True
                self.click_able = False
            elif self.grid[0][2] == 'O' and self.grid[1][1] == 'O' and self.grid[2][0] == 'O':
                self.o_win += 1
                self.o_scored = True
                self.win = True
                self.click_able = False

    def final_screen(self):
        if self.win:
            self.lose = False
            self.win_screen()
        if self.lose:
            self.lose_screen()
    def win_screen(self):
        font = pygame.font.Font('newfont.ttf', SIDE * 3 // 4)
        text = font.render("X Wins", True, BLACK)
        if self.o_scored:
            text = font.render("O Wins", True, BLACK)
        box = text.get_rect()
        box.center = (((SCREEN_W - BOARD_W) // 2) + BOARD_W, BOARD_H * 0.75)
        self.window.blit(text, box)
    def lose_screen(self):
        font = pygame.font.Font('newfont.ttf', SIDE * 3 // 4)
        text = font.render("Tie", True, BLACK)
        box = text.get_rect()
        box.center = (((SCREEN_W - BOARD_W) // 2) + BOARD_W, BOARD_H * 0.75)
        self.window.blit(text, box)

