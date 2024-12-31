import pygame
from os import listdir

class Player(pygame.sprite.Sprite):
    def __init__(self,group,pos,othergroups=0):
        super().__init__(group)

        self.is_player = True
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
        self.rect = self.image.get_rect(center=(pos)) # OG: 1710, 1820; Testing: 1710, 930; New: 1695, 1820; Interior Test: 848,910
        self.hitbox = self.rect.inflate(-75,-75)
        self.direction = pygame.math.Vector2()
        self.speed = 3
        

        self.othergroups = othergroups


    def input(self):
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

        self._layer = self.rect.bottom


    def animation(self):
        if self.direction.x == 0 and self.direction.y == 0:
            self.image = self.frames[self.facing][0]
            return

        self.animation_index += 0.15
        if self.animation_index >= 5:
            self.animation_index = 1
        self.image = self.frames[self.facing][int(self.animation_index)]
        

    def get_frames(self,path):
        newlist = []
        for file in listdir(path):
            newlist.append(pygame.transform.scale(pygame.image.load(f'{path}/{file}').convert_alpha(), (100,100)))
        return newlist


    def collision_check(self,direction):
        if self.othergroups == 0:
            return

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

            # if self.hitbox.collidepoint(sprite.door):
            #     print(sprite.type)

        self.border_collision()


    def border_collision(self):
        if self.hitbox.collidepoint(0,self.hitbox.centery): self.hitbox.left = 0
        if self.hitbox.collidepoint(4096,self.hitbox.centery): self.hitbox.right = 4096
        if self.hitbox.collidepoint(self.hitbox.centerx,0): self.hitbox.top = 0
        if self.hitbox.collidepoint(self.hitbox.centerx,4096): self.hitbox.bottom = 4096  


    def update(self):
        self.input()
        self.hitbox.centerx += self.direction.x * self.speed
        self.collision_check('h')
        self.hitbox.centery += self.direction.y * self.speed
        self.collision_check('v')
        self.rect.center = self.hitbox.center
        self.animation()