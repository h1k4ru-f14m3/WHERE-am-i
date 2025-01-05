import pygame
import settings
import map
import sys
from math import sqrt

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()

        # Note to self: scale down the interior to 896 for police department

        if settings.onMainMap:
            self.map_surf = pygame.transform.scale2x(pygame.image.load('resources/maps/test-map-7.png').convert_alpha())
            self.map_rect = self.map_surf.get_rect(center = (0,0))

        # map.render_map("House-1",self)

        self.offset = pygame.math.Vector2()
        self.half_w = self.screen.get_size()[0] / 2 
        self.half_h = self.screen.get_size()[1] / 2

    
    def update_layer(self,player):
        closest_distance = sys.maxsize
        closest_sprite = 0
        for sprite in self.sprites():
            if sprite == player or sprite.z in [0, 5]: continue
            x = abs(player.rect.center[0] - sprite.rect.center[0])
            y = abs(player.rect.center[1] - sprite.rect.center[1])
            distance = sqrt(x**2 + y**2)
            if distance <= closest_distance:
                closest_distance = distance
                closest_sprite = sprite

        if closest_sprite == 0: return
        if closest_sprite.z in [3,6] and player.rect.center[1] < closest_sprite.rect.center[1]:
            player.z = closest_sprite.z - 1
            return
        player.z = closest_sprite.z

        

    def render(self,player):

        # Player Centered

        # Minus 400 of Original Map's X Size
        # if player.centerx < 3696 and player.centerx > 400:
        #     self.offset.x = -(player.center[0] - self.screen.get_size()[0] / 2)
        # if player.centery < 3796 and player.centery > 300:
        #     self.offset.y = -(player.center[1] - self.screen.get_size()[1] / 2)

        self.offset.x = -(player.center[0] - self.screen.get_size()[0] / 2)
        self.offset.y = -(player.center[1] - self.screen.get_size()[1] / 2)

        if settings.onMainMap:
            self.screen.blit(self.map_surf,self.map_rect.center + self.offset)

        # for sprite in sorted(self.sprites(), key= lambda x: x.hitbox.centery):
        for sprite in sorted(self.sprites(), key=lambda sprite: (sprite.z,sprite.y_sort)):
            self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)
