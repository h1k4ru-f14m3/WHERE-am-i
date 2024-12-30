import pygame
import pytmx.util_pygame
from settings import map_tiles,object_sprites,all_sprites,draworder
from sprites import GameSprite


file_path = "resources/maps"


def render_map(type,group,collision_group):
    mapdata = pytmx.load_pygame(f"{file_path}/{type}/{type}.tmx", pixelalpha=True)

    # Tile Layers
    for layer in mapdata.visible_tile_layers:
        for x,y,img in mapdata.layers[layer].tiles():
            name = mapdata.layers[layer].name
            sprite = GameSprite((x * 32 * 2.5, y * 32 * 2.5), img, (group))

            # Add the sprites into their specific groups
            if name == "Ground": map_tiles.add(sprite)
            else:
                all_sprites[name].add(sprite)


    # Objects
    for layer in mapdata.visible_object_groups:
        for obj in mapdata.layers[layer]:
            name = mapdata.layers[layer].name
            sprite = GameSprite(((obj.x * 2.5), (obj.y * 2.5)), obj.image, (group), width=obj.width, height=obj.height)

            all_sprites[name].add(sprite)


    # Hitboxes
    for layer in mapdata.objectgroups:
        if "Hitbox" not in layer.name:
            continue
        
        for obj in layer:
            GameSprite(((obj.x * 2.5), (obj.y * 2.5)), pygame.surface.Surface((obj.width,obj.height)), (collision_group), width=obj.width,height=obj.height)
