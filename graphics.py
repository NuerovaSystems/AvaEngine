import pygame

class Graphics:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background_color = (30, 30, 120)
        print("Graphics loaded")

    def render(self, player, backgrounds, enemies):
        self.screen.fill(self.background_color)

        # Keep player centered
        camera_x = player.x - self.width // 2
        camera_y = player.y - self.height // 2

        for obj in backgrounds:
            obj.draw(self.screen, camera_x, camera_y)
        for enemy in enemies:
            enemy.draw(self.screen, camera_x, camera_y)
        player.draw(self.screen, self.width // 2, self.height // 2)

        pygame.display.flip()

    def render_game_over(self, message="Game Over - Press R to Restart or Q to Quit"):
        # draw a semi-transparent overlay and centered text
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        try:
            font = pygame.font.SysFont(None, 48)
        except Exception:
            pygame.font.init()
            font = pygame.font.SysFont(None, 48)

        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()