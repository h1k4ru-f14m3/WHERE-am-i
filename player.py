import pygame
import settings
from map import getin_building
from time import sleep
from os import listdir

class Player(pygame.sprite.Sprite):
    def __init__(self,group,pos,othergroups=0):
        # Get the parent class' functions
        super().__init__(group)

        # Importing player frames and preparing to render player
        file_path = 'resources/entities/player'
        self.animation_index = 0
        self.facing = 'front'
        self.frames = {
            'back': [self.get_frames(file_path)[i] for i in range(0,5)],
            'front': [self.get_frames(file_path)[i] for i in range(5,10)],
            'left': [self.get_frames(file_path)[i] for i in range(10,15)],
            'right': [self.get_frames(file_path)[i] for i in range(15,20)]
        }
        self.image = self.frames[self.facing][self.animation_index]

        # Setting player hitbox and position
        self.rect = self.image.get_rect(center=(pos)) # OG: 1710, 1820; Testing: 1710, 930; New: 1695, 1820; Interior Test: 848,910
        self.hitbox = self.rect.inflate(-75,-75)

        # Regarding player movement
        self.direction = pygame.math.Vector2()
        self.speed = 3

        # Regarding draw order of player
        self.z = settings.draw_order["Player"]
        self.y_sort = self.rect.centery

        # Regarding the groups the player sprite is in and the group to check the collisions
        self.group = group
        self.othergroups = othergroups



    def input(self):
        # Player movement and setting which type of player sprite frame to display
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.facing = 'back'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.facing = 'front'
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
            self.facing = 'left'
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.facing = 'right'
        else:
            self.direction.x = 0



    def animation(self):
        # If the player is still, display the static frame of the player depending on its current facing/direction
        if self.direction.x == 0 and self.direction.y == 0:
            self.image = self.frames[self.facing][0]
            return

        # Loop through animation frames, animation index sets the speed/fps of the animation
        self.animation_index += 0.15
        if self.animation_index >= 5:
            self.animation_index = 1
        self.image = self.frames[self.facing][int(self.animation_index)]
        


    def get_frames(self,path):
        # A function to import the player frames. (Made this function for code organization sake)
        newlist = []
        for file in sorted(listdir(path), key=lambda x: x.lower()):
            newlist.append(pygame.transform.scale(pygame.image.load(f'{path}/{file}').convert_alpha(), (100,100)))
        return newlist



    def collision_check(self,direction):
        # Doing the function of some collisions if the player collides with them
        self.collision_functions()

        # Collision check between normal objects
        for sprite in self.othergroups:
            if direction == 'h' and sprite.hitbox.colliderect(self.hitbox):
                if self.direction.x > 0:
                    self.hitbox.right = sprite.hitbox.left
                else:
                    self.hitbox.left = sprite.hitbox.right

            if direction == 'v' and sprite.hitbox.colliderect(self.hitbox):
                if self.direction.y > 0:
                    self.hitbox.bottom = sprite.hitbox.top
                else:
                    self.hitbox.top = sprite.hitbox.bottom

        # Checking if the player is colliding with the border
        self.border_collision()



    def border_collision(self):
        # Very self explanatory, checking if the player is hitting the border and stopping the player/setting the player pos to the part of the border its hitting
        if self.hitbox.collidepoint(0,self.hitbox.centery): self.hitbox.left = 0
        if self.hitbox.collidepoint(4096,self.hitbox.centery): self.hitbox.right = 4096
        if self.hitbox.collidepoint(self.hitbox.centerx,0): self.hitbox.top = 0
        if self.hitbox.collidepoint(self.hitbox.centerx,4096): self.hitbox.bottom = 4096  



    def collision_functions(self):
        # Checking collisions
        for sprite in self.othergroups:
            
            # Going out of buildings
            if sprite.name == 'door' and sprite.hitbox.colliderect(self.hitbox):
                print("1")
                self.group.unload_map(self)
                self.group.load_main()
                self.hitbox.centerx = settings.ending[0]
                self.hitbox.centery = settings.ending[1] + 25

                settings.current_floor = 0
                settings.stair_end = (0,0)
                settings.onMainMap = True
                settings.inBuilding = False
                settings.building = "None"
                return
            
            # Going upstairs of a building, if upstairs exists
            elif sprite.name == 'stair' and sprite.hitbox.colliderect(self.hitbox):
                self.group.unload_map(self)
                if settings.current_floor == 1:
                    getin_building((self.group), self, settings.building,floor_num = settings.current_floor + 1)
                    settings.current_floor += 1
                else:
                    getin_building((self.group), self, settings.building,floor_num = settings.current_floor - 1)
                    settings.current_floor -= 1
                
                print("1")
            
            # Going into buildings
            elif settings.onMainMap and self.hitbox.collidepoint(sprite.door):
                print("2")
                print(sprite.type)
                settings.ending = self.hitbox.center

                if sprite.type == "House-3": settings.current_floor = 1
                getin_building((self.group), self, sprite.type,floor_num=settings.current_floor)



    def update(self):
        # Updating everything
        self.y_sort = self.rect.centery
        self.input()

        self.hitbox.centerx += self.direction.x * self.speed
        self.collision_check('h')
        self.hitbox.centery += self.direction.y * self.speed
        self.collision_check('v')
        
        self.rect.center = self.hitbox.center
        self.animation()