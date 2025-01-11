import pygame
import string


class Buildings(pygame.sprite.Sprite):
    def __init__(self, group, type, pos, hitbox_size, z=1, name="None"):
        # Get functions from parent class
        super().__init__(group)
        
        # Name and import image (Name is here so it wouldn't generate errors, mainly)
        self.name = name
        self.image = pygame.transform.scale2x(pygame.image.load(f'resources/buildings/{type.lower()}.png').convert_alpha())

        # Setting the hitbox and the door to enter
        self.rect = self.image.get_rect(midbottom=(pos))
        self.hitbox = self.rect.inflate((hitbox_size))
        self.hitbox.midbottom = pos
        self.door = self.hitbox.midbottom

        # Type to differenciate buildings
        self.type = type
        self.z = z
        self.y_sort = self.hitbox.centery + 100
        if type == 'Mart': self.door = ((self.hitbox.midbottom[0] + 140), (self.hitbox.midbottom[1]))
        
        

# Values to input:
#   List of x pos (X pos to place the buildings)
#   List of y pos (Y pos to place the buildings/Row count and its positions)
#   List of counts for each y pos(e.g. 3 building for the first y pos)
buildings_group = pygame.sprite.Group()
def build(x_pos,y_pos,counts,group,name,hitbox):
    index = 0
    for i in range(len(y_pos)):
        for j in range(len(x_pos)):
            if j >= counts[i]:
                break
            
            buildings_group.add(Buildings(group,name,(x_pos[index],y_pos[i]),(hitbox)))
            index += 1


# Build all buildings and put them into group
def buildall(group):
    y_pos_list = [572,1754,2694,3870]

    # Police Department
    Buildings((group, buildings_group),'Police-Department',(1690,y_pos_list[1]),(-150,-275))

    # Tom's Diner
    Buildings((group, buildings_group),'Toms-Diner',(1668,y_pos_list[0]),(-75,-425))

    # Mart
    Buildings((group, buildings_group),'Mart',(3522,y_pos_list[1]),(-265,-475))

    # House 1
    house1_x = [1666,2924]
    house1_y = [y_pos_list[3]]
    house1_counts = [2]
    build(house1_x,house1_y,house1_counts,(group, buildings_group),'House-1',(-180,-275))

    # House 2
    house2_x = [404,2902,3734,3600,966]
    house2_y = [y_pos_list[i] for i in [0,2,3]]
    house2_counts = [3,1,1]
    build(house2_x,house2_y,house2_counts,(group, buildings_group),'House-2',(-180,-275))

    # House 3
    house3_x = [614,1022,1708,2900,3756,302]
    house3_y = [y_pos_list[i] for i in [1,2,3]] # Idea/Code suggested by cs50.ai
    house3_counts = [1,3,2]
    build(house3_x,house3_y,house3_counts,(group, buildings_group),'House-3',(-180,-275))
