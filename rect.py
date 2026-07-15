import pygame

class Rect:
    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen, camera_x, camera_y):
        # Draw relative to camera/player position
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        pygame.draw.rect(screen, self.color, (screen_x, screen_y, self.width, self.height))