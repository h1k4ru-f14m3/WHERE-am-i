import pygame
import settings
from player import Player
from camera import Camera
from buildings import buildall,buildings_group


class Game():
    def __init__(self,clock):
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
        while settings.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.running = False

            self.screen.fill('black')
            self.camera.render(self.player.rect)

            if settings.isPlaying:
                self.camera.update_layer(self.player)
                self.camera.update()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()