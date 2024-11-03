import pygame

pygame.init()

screen_size = 600
n = 8
cell_size = screen_size // n

screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Logic Magnet")


def draw_board():
    screen.fill(WHITE)
    for row in tiles:
        for tile in row:
            pygame.draw.rect(screen, (200, 200, 200), tile['rect'], 1)