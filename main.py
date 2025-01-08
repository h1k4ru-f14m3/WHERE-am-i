import pygame
from player import Player
from camera import Camera
from buildings import Buildings,buildall,buildings_group
import settings
from time import sleep
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

# Initialize Main-Map
buildall(camera)
settings.active_sprites.add(buildings_group)

# Initialize Player (1685,1850) (475,860)
player = Player(camera,(1685,1850),settings.active_sprites)

# Testing player pos
player_pos = player.rect.center
font = pygame.font.Font('resources/menu/fonts/upheavtt.ttf',35)
text_surf = font.render(f'Pos: ({player_pos[0]}, {player_pos[1]})', True, (255,255,255))
text2_surf = font.render(f'Offset: ({camera.offset[0]}, {camera.offset[1]})', True, (255,255,255))
text_rect = text_surf.get_rect(center=(400,50))
text2_rect = text2_surf.get_rect(center=(400,75))


# Game Loop
while settings.running:
    for event in pygame.event.get():
        # If user quits
        if event.type == pygame.QUIT:
            settings.running = False

    # Fill the screen with black so the sprites won't look weird if there's nothing to render
    screen.fill('black')

    # Render and update the player's z value dynamically for drawing order
    camera.render(player.rect)

    # Temporary Key binds
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        if settings.isPlaying:
            settings.isPlaying = False
        else: 
            settings.isPlaying = True
    if keys[pygame.K_m]: 
        camera.unload_map(player)
        camera.load_main()

        settings.onMainMap = True
        settings.inBuilding = False
        settings.building = "None"
    if keys[pygame.K_1]:
        camera.unload_map(player)
        render_map("House-1",camera,settings.active_sprites)
        player.hitbox.center = (settings.starting)

        settings.onMainMap = False
        settings.inBuilding = True
        settings.building = "House-1"
    if keys[pygame.K_2]:
        camera.unload_map(player)
        render_map("House-2",camera,settings.active_sprites)
        player.hitbox.center = (settings.starting)

        settings.onMainMap = False
        settings.inBuilding = True
        settings.building = "House-2"
    if keys[pygame.K_t]:
        camera.unload_map(player)
        render_map("Toms-Diner",camera,settings.active_sprites)
        player.hitbox.center = (settings.starting)

        settings.onMainMap = False
        settings.inBuilding = True
        settings.building = "Toms-Diner"
    if keys[pygame.K_DELETE]:
        camera.unload_map(player)

        settings.onMainMap = False
        settings.inBuilding = False

    # Testing purposes(Player Pos)
    player_pos = player.rect.center
    text_surf = font.render(f'Pos: ({player_pos[0]}, {player_pos[1]})', True, (255,255,255))
    text2_surf = font.render(f'Offset: ({camera.offset[0]}, {camera.offset[1]})', True, (255,255,255))
    screen.blit(text_surf,text_rect)
    screen.blit(text2_surf,text2_rect)

    # Keep updating the screen
    if settings.isPlaying:
        camera.update_layer(player)
        camera.update()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()