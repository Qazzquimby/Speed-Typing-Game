import pygame

class Screen:

    def __init__(self, x_size, y_size):
        self.X_size = x_size
        self.Y_size = y_size
        self.screen_size = (self.X_size, self.Y_size)
        self.color_white = (255, 255, 255)
        self.color_black = (0, 0, 0)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.font = pygame.font.Font(None, 32)

    def setup(self):
        pygame.display.set_caption("SpeedTypo")
