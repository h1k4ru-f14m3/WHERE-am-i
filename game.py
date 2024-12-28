import pygame
from player import Player
from camera import Camera
from buildings import Buildings,buildall,buildings_group
import settings
from map import render_map


# Initialize Pygame
pygame.init()

# The Window/Screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_icon(pygame.image.load('resources/entities/player/detective-front-static.png').convert_alpha())
pygame.display.set_caption('WHO (did it?)')

# Initialize the clock
clock = pygame.time.Clock()

# Initialize Camera
camera = Camera()

# Initialize Buildings
# buildall(camera)

# # Active Sprites for collisions
# settings.active_sprites.add(buildings_group)

# Initialize Map
if settings.onMainMap:
    buildall(camera)
    settings.active_sprites.add(buildings_group)
else:
    render_map("House-1",camera,settings.active_sprites)

# Initialize Player (1685,1850)
player = Player(camera,(475,860),settings.active_sprites)

# Is game running?
running = True

# Testing player pos
player_pos = player.rect.center
font = pygame.font.Font(None,35)
text_surf = font.render(f'Pos: ({player_pos[0]}, {player_pos[1]})', True, (255,255,255))
text2_surf = font.render(f'Offset: ({camera.offset[0]}, {camera.offset[1]})', True, (255,255,255))
text_rect = text_surf.get_rect(center=(400,50))
text2_rect = text2_surf.get_rect(center=(400,75))



# Game Loop
while running:
    for event in pygame.event.get():
        # If user quits
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')
    camera.render(player.rect)
    camera.update()

    # Testing purposes(Player Pos)
    player_pos = player.rect.center
    text_surf = font.render(f'Pos: ({player_pos[0]}, {player_pos[1]})', True, (255,255,255))
    text2_surf = font.render(f'Offset: ({camera.offset[0]}, {camera.offset[1]})', True, (255,255,255))
    screen.blit(text_surf,text_rect)
    screen.blit(text2_surf,text2_rect)

    # Keep updating the screen
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()