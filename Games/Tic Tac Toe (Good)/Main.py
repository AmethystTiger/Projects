import pygame
from tictactoe.tic_build import Build
from tictactoe.constants import SCREEN_W, SCREEN_H, WHITE

pygame.init()

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load('tic_icon.ico')
pygame.display.set_icon(icon)

def main():
    clock = pygame.time.Clock()
    run = True
    build = Build(screen)

    while run:
        clock.tick(60)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        build.main_game()

        pygame.display.update()
    pygame.quit()


main()
