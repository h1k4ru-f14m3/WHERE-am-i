import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self,pos,image,group,layer=0,width=32,height=32):
        super().__init__(group)
        self.image = pygame.transform.scale(image,(width * 2.5,height * 2.5))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect
        self._layer = layer