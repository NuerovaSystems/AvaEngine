# Example for bush.py
import pygame

class Bush:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.color = (34, 139, 34)

    def draw(self, screen, camera_x, camera_y):
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        pygame.draw.rect(screen, self.color, (screen_x, screen_y, self.width, self.height))