import pygame
import pytmx.util_pygame
import settings
from sprites import GameSprite
from os import path


def render_map(type,group,collision_group,floornum=0):
    file_path = "resources/maps"
    floor = str()
    if floornum != 0:
        floor = "-floor-" + f"{floornum}"
    file = path.join(file_path, type, f"{type}{floor}.tmx")
    if not path.exists(file): 
        return

    mapdata = pytmx.load_pygame(file, pixelalpha=True)

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
            name = "None"
            if obj.name == "door" or obj.name == "stair": 
                name = obj.name
            GameSprite(((obj.x * 2.5), (obj.y * 2.5)), pygame.surface.Surface((obj.width,obj.height)), (collision_group), width=obj.width,height=obj.height,name=name)

    for marker in mapdata.get_layer_by_name("Marker"):
        if marker.name == "start":
            settings.starting = (marker.x * 2.5, marker.y * 2.5)
        elif marker.name == "stair_end":
            settings.stair_end = (marker.x * 2.5, marker.y * 2.5)

    # for obj in mapdata.get_layer_by_name("Door"):
    #     GameSprite(((obj.x * 2.5), (obj.y * 2.5)), obj.image, (group))
        

def getin_building(group,player,type,floor_num=0):
    group.unload_map(player)
    render_map(type,group,settings.active_sprites,floornum=floor_num)

    if floor_num == 1 and settings.current_floor == 2:
        player.hitbox.center = (settings.stair_end)
    else:
        player.hitbox.center = (settings.starting)

    settings.onMainMap = False
    settings.inBuilding = True
    settings.building = type
    


    


