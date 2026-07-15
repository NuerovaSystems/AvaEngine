import pygame
from graphics import Graphics
from player import Player
from bush import Bush
from road import Road
from enemy import Enemy

WIDTH, HEIGHT = 800, 600

engine = Graphics(WIDTH, HEIGHT)
player = Player(0, 0)
backgrounds = []
enemies = []

selected_type = "bush"
running = True
game_over = False
clock = pygame.time.Clock()

def is_colliding(a, b):
    return (
        a.x < b.x + b.width and
        a.x + a.width > b.x and
        a.y < b.y + b.height and
        a.y + a.height > b.y
    )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selected_type = "bush"
            elif event.key == pygame.K_2:
                selected_type = "road"
            elif event.key == pygame.K_3:
                selected_type = "enemy"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            camera_x = player.x - WIDTH // 2
            camera_y = player.y - HEIGHT // 2
            wx = mx + camera_x
            wy = my + camera_y
            if selected_type == "bush":
                backgrounds.append(Bush(wx, wy))
            elif selected_type == "road":
                backgrounds.append(Road(wx, wy))
            elif selected_type == "enemy":
                enemies.append(Enemy(wx, wy))
            print(f"Placed {selected_type} at world coordinates ({wx}, {wy})")

    keys = pygame.key.get_pressed()
    speed = 5
    if not game_over:
        if keys[pygame.K_LEFT]: player.x -= speed
        if keys[pygame.K_RIGHT]: player.x += speed
        if keys[pygame.K_UP]: player.y -= speed
        if keys[pygame.K_DOWN]: player.y += speed

    # ---- Collision and attack logic happens here, every frame ----
    for enemy in enemies[:]:  # iterate a copy so we can remove safely
        if not game_over and is_colliding(player, enemy):
            if keys[pygame.K_SPACE]:
                enemy.health -= 1
                if enemy.health <= 0:
                    enemies.remove(enemy)
            else:
                player.health -= 1
                print("Player hit! Health:", player.health)
                if player.health <= 0:
                    player.death()
                    print("Player died — entering Game Over state")
                    game_over = True
    # -------------------------------------------------------------

    engine.render(player, backgrounds, enemies)

    if game_over:
        engine.render_game_over()

    # handle input during game over state
    if game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # restart: reset player, clear entities
                    player = Player(0, 0)
                    backgrounds = []
                    enemies = []
                    game_over = False
                    print("Game restarted")
                elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False

    clock.tick(60)

pygame.quit()