import pygame
import game_functions as gf

from bros import Bros

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("My Test Sky")

    # bg color
    bg_color = (135, 206, 250)

    # set bros instance
    bros = Bros(screen)

    while True:
        gf.check_events()
        """Update images on the screen and flip to the new screen."""
        """Update images on the screen and flip to the new screen."""
        # Redraw the screem during each pass through the loop.
        screen.fill(bg_color)
        bros.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

        