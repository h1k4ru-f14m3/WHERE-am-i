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
        # Check if the z property is present, if so give that tile that z value
        z = settings.draw_order[f"{mapdata.layers[layer].name}"]
        if 'z' in mapdata.layers[layer].properties:
            z = float(mapdata.layers[layer].z)

        # Load the tile
        for x,y,img in mapdata.layers[layer].tiles():
            GameSprite((x * 32 * 2.5, y * 32 * 2.5), img, (group), z=z)


    # Load the objects
    for layer in mapdata.visible_object_groups:
        for obj in mapdata.layers[layer]:
            # Check if there's a y sort offset property and z property in the object
            ysortoffset = 0
            z = settings.draw_order[f"{mapdata.layers[layer].name}"]
            if 'y_sort_offset' in obj.properties:
                ysortoffset = int(obj.y_sort_offset)
            elif 'z' in obj.properties:
                z = float(obj.z)

            # Load the Object
            GameSprite(((obj.x * 2.5), (obj.y * 2.5)), obj.image, (group), width=obj.width, height=obj.height, z=z, ysort_offset=ysortoffset)


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
        settings.markers[marker.name] = (marker.x * 2.5, marker.y * 2.5)

        
# Function to make it easier to render maps or buildings' interiors
def getin_building(group,player,type,floor_num=0,stair_num=1):
    # Unload the current map
    group.unload_map(player)
    
    # Render the desired map
    render_map(type,group,settings.active_sprites,floornum=floor_num)

    # Decide where to put the player depending on the floor and stair
    destination_up = settings.markers["stair_end"]
    destination_down = settings.markers["start"]
    if stair_num == 2: 
        destination_up = settings.markers["stair_end_2"]
        destination_down = settings.markers["start_2"]

    if floor_num == 1 and settings.current_floor == 2:
        player.hitbox.center = (destination_up)
    else:
        player.hitbox.center = (destination_down)

    # Set the booleans
    settings.onMainMap = False
    settings.inBuilding = True
    settings.building = type
    

