import pygame
import sys
from math import sqrt
import settings
import map

class Camera(pygame.sprite.LayeredUpdates):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.proximity_sprites = pygame.sprite.LayeredUpdates()
        self.y_sort_sprites = pygame.sprite.LayeredUpdates()

        if settings.onMainMap:
            self.map_surf = pygame.transform.scale2x(pygame.image.load('resources/maps/test-map-7.png').convert_alpha())
            self.map_rect = self.map_surf.get_rect(center = (0,0))


        self.offset = pygame.math.Vector2()
        self.half_w = self.screen.get_size()[0] / 2
        self.half_h = self.screen.get_size()[1] / 2


    # Comment
    def load_map(self, player):
        # Load the objects with their layer
        self.test_sprites = pygame.sprite.LayeredUpdates()
        index = 2
        for group in settings.all_sprites.values():
            for sprite in group:
                self.test_sprites.add(sprite, layer=index)
            index += 2

        self.test_sprites.add(player)
    


    def layer_change(self,player):
        player_pos = player.rect.center
        proximity = 150
        distance = 0

        for sprite in self.test_sprites:
            if sprite == player: continue
            x = abs(player_pos[0] - sprite.rect.center[0])
            y = abs(player_pos[1] - sprite.rect.center[1])

            distance = sqrt(x**2 + y**2)
            if distance <= proximity:
                self.proximity_sprites.add(sprite)
            elif sprite in self.proximity_sprites:
                self.proximity_sprites.remove(sprite)

        layers = {}
        for sprite in self.proximity_sprites:
            if sprite == player: continue
            # Add a conditional here so that sprites that have lower midbottom y than player midtop - x is skipped so it can be y sorted
            layers.update({sprite: sprite._layer})
            if player.rect.centery > sprite.rect.centery:
                self.y_sort_sprites.add(sprite, layer=self.test_sprites.get_layer_of_sprite(sprite))
            elif sprite in self.y_sort_sprites:
                self.y_sort_sprites.remove(sprite)

        closest_layer = sys.maxsize
        for i in layers.values():
            if i < closest_layer:
                closest_layer = i

        self.test_sprites.change_layer(player, closest_layer)



    def render(self,player):

        # Player Centered

        # Minus 400 of Original Map's X Size
        # if player.centerx < 3696 and player.centerx > 400:
        #     self.offset.x = -(player.center[0] - self.screen.get_size()[0] / 2)
        # if player.centery < 3796 and player.centery > 300:
        #     self.offset.y = -(player.center[1] - self.screen.get_size()[1] / 2)
        

        self.offset.x = -(player.rect.center[0] - self.screen.get_size()[0] / 2)
        self.offset.y = -(player.rect.center[1] - self.screen.get_size()[1] / 2)


        if settings.onMainMap:
            self.screen.blit(self.map_surf,self.map_rect.center + self.offset)


        # Load the Ground Layer
        for sprite in settings.map_tiles:
            self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)


        # Load Everything else except the ground
        for sprite in self.test_sprites:
            # if sprite in self.y_sort_sprites:
            #     continue
            self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)
            # print(f"{sprite}: {self.test_sprites.get_layer_of_sprite(sprite)}"

        # print(self.test_sprites.get_sprites_at(player.center))