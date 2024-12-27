import pygame
import pytmx.util_pygame
from settings import active_sprites
from sprites import GameSprite


def render_map(type,group):
    file_path = "resources/maps"
    mapdata = pytmx.load_pygame(f"{file_path}/{type}/{type}.tmx", pixelalpha=True)

    for layer in mapdata.visible_tile_layers:
        for x,y,img in mapdata.layers[layer].tiles():
            if not img:
                continue
            GameSprite((x * 32 * 2.5, y * 32 * 2.5), img, (group))

    for layer in mapdata.visible_object_groups:
        print(f"Layer {layer}: {mapdata.layers[layer]}")
        for obj in mapdata.layers[layer]:
            if not obj.image:
                continue
            GameSprite(((obj.x * 2.5), (obj.y * 2.5)), obj.image, (group), width=obj.width, height=obj.height)

    # for obj in mapdata.get_layer_by_name("Door"):
    #     GameSprite(((obj.x * 2.5), (obj.y * 2.5)), obj.image, (group))
        
    


    


