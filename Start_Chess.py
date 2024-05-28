import pygame
import sys
from Board import Board


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Chess")
    screen.fill((0, 0, 0))

    board = Board()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                board.input.handle_event(event)

        screen.fill((0, 0, 0))
        board.paint_component()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
