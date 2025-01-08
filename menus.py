import pygame
import settings
import os

class menu(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def main_menu(self,screen):
        button('long-button-large', (300,510), self, 'Play')
        button('settings-button', (400,510), self)

        while settings.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.running = False

            screen.fill('#384259')
            for sprite in self.sprites():
                sprite.update()

        pygame.quit()


class button(pygame.sprite.Sprite):
    def __init__(self, type, pos, group, text="None"):
        super().__init__(group)
        self.screen = pygame.display.get_surface()
        static_file = os.path.join('resources', 'menu', 'static', f'{type}.png')
        pressed_file = os.path.join('resources', 'menu', 'pressed', f'{type}.png')

        if text != "None":
            font_file = os.path.join('resources', 'menu', 'fonts', 'upheavtt.ff')
            font_size = 0

            if 'large' in type:
                font_size = 48
            elif 'small' in type:
                font_size = 32

            self.font = pygame.font.Font(font_file, font_size)

        self.frames = {
            's': static_file,
            'p': pressed_file
        }

        self.index = 's'
        self.image = pygame.image.load(self.frames[self.index])
        self.rect = self.image.get_rect(center=(pos))
        if text != "None":
            self.text_surf = self.font.render(text,False,'#ffffff')
            self.shadow = self.font.render(text,False,'#7AC7C4')
            self.text_rect = self.text_surf.get_rect(center=(pos))
            self.shadow_rect = self.shadow.get_rect(center=(pos[0]+15,pos[0]+15))


    def listen(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] in range(self.rect.left,self.rect.right) and mouse_pos[1] in range(self.rect.top,self.rect.bottom):
            self.index = 'p'
        else:
            self.index = 's'


    def update(self):
        self.listen()
        self.screen.blit(self.image,self.rect)
        self.screen.blit(self.text_surf,self.text_rect)
        self.screen.blit(self.shadow,self.shadow_rect)

    


