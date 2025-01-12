import pygame
import settings
import map
import buildings
import sys
from math import sqrt

class Camera(pygame.sprite.Group):
    def __init__(self):
        # Get parent class' functions
        super().__init__()

        # Get the screen to render on
        self.screen = pygame.display.get_surface()

        # Render the main map if the player is on the main map
        if settings.onMainMap:
            self.map_surf = pygame.transform.scale2x(pygame.image.load('resources/maps/main-map.png').convert_alpha())
            self.map_rect = self.map_surf.get_rect(center = (0,0))

        # Initialize values to get player centered camera
        self.offset = pygame.math.Vector2()
        self.half_w = self.screen.get_size()[0] / 2 
        self.half_h = self.screen.get_size()[1] / 2


    # Very self explanatory, load the main map
    def load_main(self):
        self.map_surf = pygame.transform.scale2x(pygame.image.load('resources/maps/test-map-7.png').convert_alpha())
        self.map_rect = self.map_surf.get_rect(center = (0,0))
        buildings.buildall(self)
        settings.active_sprites.add(buildings.buildings_group)

    
    # Set the player sprite's z value dynamically
    def update_layer(self,player):
        # Prepare the integers/values for the function
        closest_distance = sys.maxsize
        second_closest_distance = sys.maxsize
        third_closest_distance = sys.maxsize

        closest_sprite = 0
        second_closest_sprite = 0
        third_closest_sprite = 0

        # Iterate through each sprite
        for sprite in self.sprites():
            # Exclude some sprites from the following process (Filtered by their z values)
            if sprite == player or sprite.z in [0, 3.5, 3.8, 5.5, 7] or sprite.z < 0: continue

            # Subtract the x and y values of player from the sprite's
            x = abs(player.rect.center[0] - sprite.rect.center[0])
            y = abs(player.rect.center[1] - sprite.rect.center[1])

            # Pythagorean Theorem to get the distance between the player and the sprite
            distance = sqrt(x**2 + y**2)

            # Get the closest sprite and the second closest sprite
            if distance < closest_distance:
                third_closest_distance = second_closest_distance
                second_closest_distance = closest_distance
                closest_distance = distance
                third_closest_sprite = second_closest_sprite
                second_closest_sprite = closest_sprite
                closest_sprite = sprite

            elif distance < second_closest_distance:
                third_closest_distance = second_closest_distance
                second_closest_distance = distance
                third_closest_sprite = second_closest_sprite
                second_closest_sprite = sprite

            elif distance < third_closest_distance:
                third_closest_distance = distance
                third_closest_sprite = sprite

        # Give less priority to some sprites with some conditions and set the player z accordingly
        if closest_sprite == 0 or second_closest_sprite == 0 or third_closest_sprite == 0: return

        z_values = {
            closest_sprite: closest_sprite.z,
            second_closest_sprite: second_closest_sprite.z,
            third_closest_sprite: third_closest_sprite.z
        }
        
        wall_outlines = []
        walls = []
        for i in z_values.values():
            if i == 6:
                wall_outlines.append(i)
            if i == 3:
                walls.append(i)

        other = [i for i in z_values.values() if i not in wall_outlines and i not in walls]

        if len(other) >= 1:
            player.z = int(other[0])
            return
        elif len(walls) > 0:
            if player.rect.centery < list(z_values.keys())[list(z_values.values()).index(3)].rect.centery:
                player.z = 2
                return
            else:
                player.z = 3
                return
        elif closest_sprite.z == 6:
                player.z = 6-2
                return
                # player.z = 6 - 2
                # return
                
            

        # if closest_sprite.z == 6 and second_closest_sprite.z == closest_sprite.z and third_closest_sprite.z != second_closest_sprite.z:
        #     player.z = third_closest_sprite.z
        #     return
        # if second_closest_sprite.z == 3 and closest_sprite.z == 6 and player.rect.center[1] < second_closest_sprite.rect.center[1]:
        #     player.z = second_closest_sprite.z - 1
        #     return
        # elif (closest_sprite.z in [3,6] and player.rect.center[1] < closest_sprite.rect.center[1]):
        #     player.z = closest_sprite.z - 1
        #     return
        
        
        player.z = closest_sprite.z


    # Delete the sprites and hitboxes except for the player sprite from every sprite group they are in
    def unload_map(self,player):
        for sprite in self.sprites():
            if sprite == player: continue
            sprite.kill()
        for hitbox in settings.active_sprites:
            hitbox.kill()
        for door in settings.doors:
            door.kill()


    # Render/Draw/Display the sprites
    def render(self,player):

        # Check if the player is in the main map and rendering the main map if true
        if settings.onMainMap:
            # To Turn off player center camera at some point (Minus 400 of Original Map's X Size)
            if player.centerx < 3696 and player.centerx > 400:
                self.offset.x = -(player.center[0] - self.screen.get_size()[0] / 2)
            if player.centery < 3796 and player.centery > 300:
                self.offset.y = -(player.center[1] - self.screen.get_size()[1] / 2)

            self.screen.blit(self.map_surf,self.map_rect.center + self.offset)

        else:
        
            # Set the offset to achieve player centered camera
            self.offset.x = -(player.center[0] - self.screen.get_size()[0] / 2)
            self.offset.y = -(player.center[1] - self.screen.get_size()[1] / 2)

        # Render the sprites (Sorted by the z value first then the y_sort value)
        for sprite in sorted(self.sprites(), key=lambda sprite: (sprite.z,sprite.y_sort)):
            self.screen.blit(sprite.image,sprite.rect.topleft + self.offset)
