# Example for road.py
import pygame

class Road:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.color = (139, 69, 19)  # tan

    def draw(self, screen, camera_x, camera_y):
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        pygame.draw.rect(screen, self.color, (screen_x, screen_y, self.width, self.height))