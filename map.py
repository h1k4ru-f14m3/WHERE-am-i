import pygame
import pytmx.util_pygame
import settings
from sprites import GameSprite
from os import path


# Load the map
def render_map(type,group,collision_group,floornum=0):
    # File path of maps
    file_path = "resources/maps"

    # Checking which floor to render. If 0, ground floor or the building doesn't have 2nd floor.
    floor = str()
    if floornum != 0:
        floor = "-floor-" + f"{floornum}"

    # Check if the file exists, if not there's nothing to render so it will be blank on the screen
    file = path.join(file_path, type, f"{type}{floor}.tmx")
    if not path.exists(file): 
        return

    # Load the .tmx file
    mapdata = pytmx.load_pygame(file, pixelalpha=True)


    # Load the tile layers
    for layer in mapdata.visible_tile_layers:
        for x,y,img in mapdata.layers[layer].tiles():
            GameSprite((x * 32 * 2.5, y * 32 * 2.5), img, (group), z=settings.draw_order[f"{mapdata.layers[layer].name}"])


    # Load the objects
    for layer in mapdata.visible_object_groups:
        for obj in mapdata.layers[layer]:
            ysortoffset = 0
            if 'y_sort_offset' in obj.properties:
                ysortoffset = int(obj.y_sort_offset)
            GameSprite(((obj.x * 2.5), (obj.y * 2.5)), obj.image, (group), width=obj.width, height=obj.height, z=settings.draw_order[f"{mapdata.layers[layer].name}"], ysort_offset=ysortoffset)


    # Load the Hitboxes and giving them names if they have one
    for layer in mapdata.objectgroups:
        if "Hitbox" not in layer.name:
            continue
        
        for obj in layer:
            name = "None"
            if obj.name: 
                name = obj.name
            GameSprite(((obj.x * 2.5), (obj.y * 2.5)), pygame.surface.Surface((obj.width,obj.height)), (collision_group), width=obj.width,height=obj.height,name=name)


    # Load the Markers and store their values
    for marker in mapdata.get_layer_by_name("Marker"):
        if marker.name == "start":
            settings.starting = (marker.x * 2.5, marker.y * 2.5)
        elif marker.name == "stair_end":
            settings.stair_end = (marker.x * 2.5, marker.y * 2.5)

        
# Function to make it easier to render maps or buildings' interiors
def getin_building(group,player,type,floor_num=0):
    # Unload the current map
    group.unload_map(player)

    # Render the desired map
    render_map(type,group,settings.active_sprites,floornum=floor_num)

    # Decide where to put the player depending on the floor
    if floor_num == 1 and settings.current_floor == 2:
        player.hitbox.center = (settings.stair_end)
    else:
        player.hitbox.center = (settings.starting)

    # Set the booleans
    settings.onMainMap = False
    settings.inBuilding = True
    settings.building = type
    


    


