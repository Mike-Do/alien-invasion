import pygame

class Bros():
    def __init__(self, screen):
    """Let's make the Bros and set their position."""
    self.screen = screen

    # Load the Bros and get there rect
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # Start the Bros at the center of the screen.
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the Bros at the bottom."""
        self.screen.blit(self.image, self.rect)


