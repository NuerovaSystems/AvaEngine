import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.color = (0, 200, 255)
        self.health = 3  # <-- move this here!
        self.alive = True
    
    def is_colliding(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )
    
    def death(self):
        if self.health <= 0 and self.alive:
            self.health = 0
            self.alive = False
            print("Player has died!")
            # Do NOT use `del self` here; other modules hold references.
            # Use the `alive` flag or notify a manager to remove the player.
        # or handle death in a more game-appropriate way

    def draw(self, screen, draw_x, draw_y):
        pygame.draw.rect(screen, self.color, (draw_x, draw_y, self.width, self.height))
