import pygame
import settings
from player import Player
from camera import Camera
from buildings import buildall,buildings_group
from time import sleep


class Game():
    def __init__(self,clock):
        # For the window
        self.screen = pygame.display.get_surface()
        self.clock = clock

        # Initialize Camera
        self.camera = Camera()

        # Initialize Main-Map
        buildall(self.camera)
        settings.active_sprites.add(buildings_group)

        # Initialize Player (1685,1850) (475,860)
        self.player = Player(self.camera,(1685,1850),settings.active_sprites)


    def run(self):
        # Game Loop
        while settings.running and settings.isPlaying:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.isPlaying = False
                    settings.running = False
                # Checking for keyboard input to show the Pause Menu
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.screen.fill('black')
                    sleep(0.25)
                    settings.isPlaying = False
                    settings.onPause = True

            # Background Color
            self.screen.fill('black')

            # Render Everything
            self.camera.render(self.player.rect)

            # Keep updating the sprites if the player is still playing
            if settings.isPlaying:
                self.camera.update_layer(self.player)
                self.camera.update()

            # Update Display/Window
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)