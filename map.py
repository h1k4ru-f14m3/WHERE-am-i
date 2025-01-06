import pygame
import pytmx.util_pygame
import settings
from sprites import GameSprite


def render_map(type,group,collision_group):
    file_path = "resources/maps"
    mapdata = pytmx.load_pygame(f"{file_path}/{type}/{type}.tmx", pixelalpha=True)

    for layer in mapdata.visible_tile_layers:
        for x,y,img in mapdata.layers[layer].tiles():
            GameSprite((x * 32 * 2.5, y * 32 * 2.5), img, (group), z=settings.draw_order[f"{mapdata.layers[layer].name}"])

    for layer in mapdata.visible_object_groups:
        for obj in mapdata.layers[layer]:
            GameSprite(((obj.x * 2.5), (obj.y * 2.5)), obj.image, (group), width=obj.width, height=obj.height, z=settings.draw_order[f"{mapdata.layers[layer].name}"])

    for layer in mapdata.objectgroups:
        if "Hitbox" not in layer.name:
            continue
        
        for obj in layer:
            GameSprite(((obj.x * 2.5), (obj.y * 2.5)), pygame.surface.Surface((obj.width,obj.height)), (collision_group), width=obj.width,height=obj.height)

    for marker in mapdata.get_layer_by_name("Marker"):
        settings.starting = (marker.x * 2.5, marker.y * 2.5)

    # for obj in mapdata.get_layer_by_name("Door"):
    #     GameSprite(((obj.x * 2.5), (obj.y * 2.5)), obj.image, (group))
        
    


    


