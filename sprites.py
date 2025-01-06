import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self,pos,image,group,width=32,height=32,ysort_offset = 0,z=0):
        super().__init__(group)
        self.image = pygame.transform.scale(image,(width * 2.5,height * 2.5))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect
        self.y_sort = self.rect.centery - ysort_offset
        self.z = z