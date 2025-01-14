import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self,pos,image,group,width=32,height=32,ysort_offset = 0,z=0,name="None"):
        super().__init__(group)
        
        # Name and import image
        self.name = name
        self.image = pygame.transform.scale(image,(width * 2.5,height * 2.5))

        # Set hitbox
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect

        # Set draw layer and prepare y sort logic
        self.y_sort = self.rect.centery - ysort_offset
        self.z = z