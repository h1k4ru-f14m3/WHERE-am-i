import pygame
import settings
import map

class Camera(pygame.sprite.LayeredUpdates):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.layered_sprites = pygame.sprite.LayeredUpdates()

        if settings.onMainMap:
            self.map_surf = pygame.transform.scale2x(pygame.image.load('resources/maps/test-map-7.png').convert_alpha())
            self.map_rect = self.map_surf.get_rect(center = (0,0))


        self.offset = pygame.math.Vector2()
        self.half_w = self.screen.get_size()[0] / 2
        self.half_h = self.screen.get_size()[1] / 2



    def load_map(self, player):
        self.test_sprites = pygame.sprite.LayeredUpdates()
        index = 0
        for group in settings.all_sprites.values():
            for sprite in group:
                self.test_sprites.add(sprite, layer=index)
            index += 1

        self.test_sprites.add(player)

        
        
        


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


        # Load the Ground Layer
        for sprite in settings.map_tiles:
            self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)

        # Load Layers
        # for group in settings.all_sprites.values():
        #     if len(group) <= 0: continue
        #     for sprite in group:
        #         self.layered_sprites.add(sprite)

        for sprite in self.test_sprites:
            self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)

        # for sprite in sorted(self.sprites(), key=lambda x: x._layer):
        #     if sprite in settings.map_tiles:
        #         continue
        #     self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)
            # print(f"{sprite}: {self.get_layer_of_sprite(sprite)}")

        # Render Every Sprite except the ground layer
        # player = pygame.sprite.LayeredUpdates()
        # player.add([sprite for sprite in self.sprites() if sprite not in self.layered_sprites.sprites() and sprite not in settings.map_tiles])

        # all_sprites = list(self.layered_sprites.sprites() + [sprite for sprite in self.sprites() if sprite not in self.layered_sprites.sprites() and sprite not in settings.map_tiles])
        
        # wall_outlines = [sprite for group in range(1,4) for sprite in settings.all_sprites[f"Wall-Outline-{group}"]]
        # sorted_sprites = sorted(all_sprites, key=lambda x: x.hitbox.centery)

        # test_sprites = pygame.sprite.LayeredUpdates()
        # test_sprites.add([player.sprites() + wall_outlines])
        # sorted_test_sprites = sorted(test_sprites, key=lambda x: x._layer)

        # for sprite in sorted_test_sprites:
        #     self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)


        # for sprite in player:
        #     self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)

        # for sprite in wall_outlines:
        #     self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)

        # self.screen.blit(player_sprite.image,player_sprite.rect.topleft + self.offset)

        # for sprite in sorted(all_sprites, key=lambda x: x._layer):
        #     self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)

        


