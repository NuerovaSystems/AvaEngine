# Example for enemy.py
import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.color = (255, 0, 0) #red
        self.health = 3  # or whatever you like
    def is_colliding(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )

    def draw(self, screen, camera_x, camera_y):
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        pygame.draw.rect(screen, self.color, (screen_x, screen_y, self.width, self.height))


def process_collisions(player, enemies, keys):
    """Handle collisions between player and enemies.
    Call from your game loop with current keys state.
    """
    for enemy in enemies[:]:  # iterate a copy so we can remove safely
        if enemy.is_colliding(player):
            # Player takes damage (add cooldown if you like)
            player.health -= 1  # maybe limit damage rate
            print("Player hit! Health:", player.health)
            if keys[pygame.K_SPACE]:
                enemy.health -= 1
                print("Enemy hit! Health:", enemy.health)
                if enemy.health <= 0:
                    enemies.remove(enemy)

    