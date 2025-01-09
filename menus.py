import pygame
import settings
import os
from time import sleep

class Menu(pygame.sprite.Group):
    def __init__(self,clock):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.clock = clock

        self.font_file = os.path.join('resources', 'menu', 'fonts', 'upheavtt.ttf')

        self.logo_font = pygame.font.Font(self.font_file, 64)
        self.logo_text = self.logo_font.render('WHERE (am i)', False, '#ffffff')
        self.logo_shadow = self.logo_font.render('WHERE (am i)', False, '#7AC7C4')
        self.logo_text_rect = self.logo_text.get_rect(center=(400,67))
        self.logo_shadow_rect = self.logo_shadow.get_rect(center=((self.logo_text_rect.centerx + 5), (self.logo_text_rect.centery + 5)))
        
        self.hint_font = pygame.font.Font(self.font_file, 32)
        self.hint_text = self.hint_font.render('Press ESC to go back...', False, '#ffffff')
        self.hint_shadow = self.hint_font.render('Press ESC to go back...', False, '#7AC7C4')
        self.hint_text_rect = self.hint_text.get_rect(center=(400,550))
        self.hint_shadow_rect = self.hint_shadow.get_rect(center=((self.hint_text_rect.centerx + 3), (self.hint_text_rect.centery + 3)))


    def main_menu(self):
        player_img = pygame.image.load('resources/entities/player/detective-front-static.png').convert_alpha()
        player_surf = pygame.transform.scale(player_img, (256,256))
        player_rect = player_surf.get_rect(center=(400,267))

        button('play', 'long-button-large', (346,480), self, 'Play')
        button('settings', 'settings-button', (600,480), self)

        while settings.running and settings.onMainMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.onMainMenu = False
                    settings.running = False

            self.screen.fill('#384259')
            self.screen.blit(player_surf,player_rect)
            self.screen.blit(self.logo_shadow,self.logo_shadow_rect)
            self.screen.blit(self.logo_text,self.logo_text_rect)
            for sprite in self.sprites():
                sprite.update()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)


    def settings_menu(self):
        logo_text = self.logo_font.render('Settings', False, '#ffffff')
        logo_text_rect = logo_text.get_rect(center=(400,67))
        logo_shadow = self.logo_font.render('Settings', False, '#7AC7C4')
        logo_shadow_rect = logo_shadow.get_rect(center=((logo_text_rect.centerx + 5), (logo_text_rect.centery + 5)))

        labels = {
            'forward': ['move-forward', 'Move Forward', (355,163)],
            'left': ['move-left', 'Move Left', (355, 243)],
            'backward': ['move-backward', 'Move Backward', (355, 323)],
            'right': ['move-right', 'Move Right', (355, 403)],
            'sound': ['sound', 'Sound', (355, 483)]
        }

        for key in labels.keys():
            button(labels[key][0], 'long-button-small', labels[key][2], self, labels[key][1], listen=False)

        while settings.running and settings.onSettings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.onSettings = False
                    settings.running = False

            self.screen.fill('#384259')
            self.screen.blit(logo_shadow,logo_shadow_rect)
            self.screen.blit(logo_text,logo_text_rect)
            self.screen.blit(self.hint_shadow,self.hint_shadow_rect)
            self.screen.blit(self.hint_text,self.hint_text_rect)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.screen.fill('black')
                sleep(0.25)
                for sprite in self.sprites():
                    sprite.kill()
                settings.onSettings = False
                settings.onMainMenu = True

            for sprite in self.sprites():
                sprite.update()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)


    def pause_menu(self):
        player_img = pygame.image.load('resources/entities/player/detective-front-static.png').convert_alpha()
        player_surf = pygame.transform.scale(player_img, (256,256))
        player_rect = player_surf.get_rect(center=(400,267))

        button('main-menu', 'long-button-large', (400,480), self, 'Main Menu')

        while settings.running and settings.onPause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.onPause = False
                    settings.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.screen.fill('black')
                sleep(0.25)
                for sprite in self.sprites():
                    sprite.kill()
                settings.onPause = False
                settings.isPlaying = True

            self.screen.fill('#384259')

            self.screen.blit(player_surf,player_rect)

            self.screen.blit(self.logo_shadow,self.logo_shadow_rect)
            self.screen.blit(self.logo_text,self.logo_text_rect)

            self.screen.blit(self.hint_shadow,self.hint_shadow_rect)
            self.screen.blit(self.hint_text,self.hint_text_rect)

            for sprite in self.sprites():
                sprite.update()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)


class button(pygame.sprite.Sprite):
    def __init__(self, name, type, pos, group, text="None", listen=True):
        super().__init__(group)
        self.name = name
        self.doListen = listen
        self.group = group
        self.screen = pygame.display.get_surface()
        self.hasText = False
        static_file = os.path.join('resources', 'menu', 'static', f'{type}.png')
        pressed_file = os.path.join('resources', 'menu', 'pressed', f'{type}.png')

        if text != "None":
            self.hasText = True
            font_file = os.path.join('resources', 'menu', 'fonts', 'upheavtt.ttf')
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
            self.shadow_rect = self.shadow.get_rect(center=(pos[0]+3,pos[1]+3))


    def listen(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_hover = (mouse_pos[0] in range(self.rect.left,self.rect.right) and mouse_pos[1] in range(self.rect.top,self.rect.bottom))
        mouse_press = (pygame.mouse.get_pressed()[0])
        if mouse_hover:
            self.index = 'p'
        else:
            self.index = 's'

        if self.name == 'play' and mouse_hover and mouse_press:
            self.screen.fill('black')
            sleep(0.25)
            for sprite in self.group.sprites():
                sprite.kill()
            settings.onMainMenu = False
            settings.isPlaying = True
        elif self.name == 'settings' and mouse_hover and mouse_press:
            self.screen.fill('black')
            sleep(0.25)
            for sprite in self.group.sprites():
                sprite.kill()
            settings.onMainMenu = False
            settings.onSettings = True
        elif self.name == 'main-menu' and mouse_hover and mouse_press:
            self.screen.fill('black')
            sleep(0.25)
            for sprite in self.group.sprites():
                sprite.kill()
            settings.onMainMenu = True
            settings.onPause = False


    def update(self):
        if self.doListen:
            self.listen()
            self.image = pygame.image.load(self.frames[self.index])

        self.screen.blit(self.image,self.rect)
        if self.hasText:
            self.screen.blit(self.shadow,self.shadow_rect)
            self.screen.blit(self.text_surf,self.text_rect)
            