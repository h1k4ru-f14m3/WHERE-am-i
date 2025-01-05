import pygame
import pytmx.util_pygame
from settings import map_tiles,object_sprites,all_sprites,all_sprites_keys
from sprites import GameSprite


file_path = "resources/maps"


def render_map(type,group,collision_group):
    mapdata = pytmx.load_pygame(f"{file_path}/{type}/{type}-floor-2.tmx", pixelalpha=True)

    # Tile Layers
    for layer in mapdata.visible_tile_layers:
        for x,y,img in mapdata.layers[layer].tiles():
            name = mapdata.layers[layer].name

            # Get the layer num
            if name == "Ground": layernum = 0
            else: layernum = all_sprites_keys.index(name) + 1 

            # Make the sprite
            sprite = GameSprite((x * 32 * 2.5, y * 32 * 2.5), img, (group), layer=layernum)

            # Add the sprites into their specific groups
            if name == "Ground": map_tiles.add(sprite)
            else:
                all_sprites[name].add(sprite)


    # Objects
    for layer in mapdata.visible_object_groups:
        for obj in mapdata.layers[layer]:
            name = mapdata.layers[layer].name
            
            # Get Layer Num
            layernum = all_sprites_keys.index(name) + 1

            sprite = GameSprite(((obj.x * 2.5), (obj.y * 2.5)), obj.image, (group), layer=layernum, width=obj.width, height=obj.height)

            all_sprites[name].add(sprite)


    # Hitboxes
    for layer in mapdata.objectgroups:
        if "Hitbox" not in layer.name:
            continue
        
        for obj in layer:
            GameSprite(((obj.x * 2.5), (obj.y * 2.5)), pygame.surface.Surface((obj.width,obj.height)), (collision_group), width=obj.width,height=obj.height)
