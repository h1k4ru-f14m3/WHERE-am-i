import pygame
import settings
import os
from music import stop_music, play_music
from time import sleep

class Menu(pygame.sprite.Group):
    def __init__(self,clock):
        super().__init__()
        # For the window
        self.screen = pygame.display.get_surface()
        self.clock = clock

        # The path of the font file
        self.font_file = os.path.join('resources', 'menu', 'fonts', 'upheavtt.ttf')

        # The Logo Text
        self.logo_font = pygame.font.Font(self.font_file, 64)
        self.logo_text = self.logo_font.render('WHERE (am i)', False, '#ffffff')
        self.logo_shadow = self.logo_font.render('WHERE (am i)', False, '#7AC7C4')
        self.logo_text_rect = self.logo_text.get_rect(center=(400,67))
        self.logo_shadow_rect = self.logo_shadow.get_rect(center=((self.logo_text_rect.centerx + 5), (self.logo_text_rect.centery + 5)))
        
        # The hint text ('Press Esc to go back...')
        self.hint_font = pygame.font.Font(self.font_file, 32)
        self.hint_text = self.hint_font.render('Press ESC to go back...', False, '#ffffff')
        self.hint_shadow = self.hint_font.render('Press ESC to go back...', False, '#7AC7C4')
        self.hint_text_rect = self.hint_text.get_rect(center=(400,550))
        self.hint_shadow_rect = self.hint_shadow.get_rect(center=((self.hint_text_rect.centerx + 3), (self.hint_text_rect.centery + 3)))


    def main_menu(self):
        # The Big Player preview Image
        player_img = pygame.image.load('resources/entities/player/detective-front-static.png').convert_alpha()
        player_surf = pygame.transform.scale(player_img, (256,256))
        player_rect = player_surf.get_rect(center=(400,267))

        # The Buttons
        button('play', 'long-button-large', (346,480), self, 'Play')
        button('settings', 'settings-button', (600,480), self)

        # Game/Window loop
        while settings.running and settings.onMainMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.onMainMenu = False
                    settings.running = False

            # Background
            self.screen.fill('#384259')

            # Player Preview
            self.screen.blit(player_surf,player_rect)

            # Logo Text
            self.screen.blit(self.logo_shadow,self.logo_shadow_rect)
            self.screen.blit(self.logo_text,self.logo_text_rect)

            # Buttons
            for sprite in self.sprites():
                sprite.update()

            # Display Update
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)


    def settings_menu(self):
        # Logo/Window Title
        logo_text = self.logo_font.render('Settings', False, '#ffffff')
        logo_text_rect = logo_text.get_rect(center=(400,67))
        logo_shadow = self.logo_font.render('Settings', False, '#7AC7C4')
        logo_shadow_rect = logo_shadow.get_rect(center=((logo_text_rect.centerx + 5), (logo_text_rect.centery + 5)))

        # Labels of settings which will not change their color upon mouse hover
        labels = {
            'forward': ['move-forward', 'Move Forward', (355,163), (638,163)],
            'left': ['move-left', 'Move Left', (355, 243), (638,243)],
            'backward': ['move-backward', 'Move Backward', (355, 323), (638,323)],
            'right': ['move-right', 'Move Right', (355, 403), (638,403)],
        }

        # sound = {
        #     'sound': ['sound', 'Sound', (355, 483), (638,483)]
        # }

        # Initialize the labels and buttons
        for key in labels.keys():
            button(labels[key][0], 'long-button-small', labels[key][2], self, labels[key][1], listen=False)
            button(labels[key][0], 'square-button-small', labels[key][3], self, pygame.key.name(settings.config[key]), listen=True)

        # Music On/Off Button and label
        button('music', 'long-button-small', (355, 483), self, 'Music', listen=False)
        button('music', f'music-button-{settings.config['sound']}', (638, 483), self, listen=True)

        # Game/Window Loop
        while settings.running and settings.onSettings:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.onSettings = False
                    settings.running = False
                # The Escape Function
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    transition(self.screen,self)
                    settings.onSettings = False
                    settings.onMainMenu = True

            # Background color
            self.screen.fill('#384259')

            # Logo/Title
            self.screen.blit(logo_shadow,logo_shadow_rect)
            self.screen.blit(logo_text,logo_text_rect)

            # Hint ('Press Esc to go back...')
            self.screen.blit(self.hint_shadow,self.hint_shadow_rect)
            self.screen.blit(self.hint_text,self.hint_text_rect)

            # Buttons
            for sprite in self.sprites():
                sprite.update()

            # Screen/Display Update
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)


    def pause_menu(self):
        # The Big Player Preview
        player_img = pygame.image.load('resources/entities/player/detective-front-static.png').convert_alpha()
        player_surf = pygame.transform.scale(player_img, (256,256))
        player_rect = player_surf.get_rect(center=(400,267))

        # Button to go to main menu
        button('main-menu', 'long-button-large', (400,480), self, 'Main Menu')

        # Game/Window Loop
        while settings.running and settings.onPause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    settings.onPause = False
                    settings.running = False
                # Escape key function
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    transition(self.screen,self)
                    settings.onPause = False
                    settings.isPlaying = True
                
            # Background color
            self.screen.fill('#384259')

            # Player Preview
            self.screen.blit(player_surf,player_rect)

            # Window/Menu Title
            self.screen.blit(self.logo_shadow,self.logo_shadow_rect)
            self.screen.blit(self.logo_text,self.logo_text_rect)

            # Hint ('Press Esc to go back...')
            self.screen.blit(self.hint_shadow,self.hint_shadow_rect)
            self.screen.blit(self.hint_text,self.hint_text_rect)

            # Buttons
            for sprite in self.sprites():
                sprite.update()

            # Screen/Display Update
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)


class button(pygame.sprite.Sprite):
    def __init__(self, name, type, pos, group, text="None", listen=True):
        super().__init__(group)
        # Name and group (name for giving functions, group for rendering/displaying/drawing)
        self.name = name
        self.group = group

        # Button or just Label
        self.doListen = listen
        
        # Screen to blit on
        self.screen = pygame.display.get_surface()

        # Self explanatory, will this have text?
        self.hasText = False

        # Location of button state image
        static_image = os.path.join('resources', 'menu', 'static', f'{type}.png')
        pressed_image = os.path.join('resources', 'menu', 'pressed', f'{type}.png')

        # If text is given
        if text != "None":
            self.hasText = True
            font_file = os.path.join('resources', 'menu', 'fonts', 'upheavtt.ttf')
            font_size = 0

            # Set font-size
            if 'large' in type:
                font_size = 48
            elif 'small' in type:
                font_size = 32

            self.font = pygame.font.Font(font_file, font_size)

        # Button state, image and position
        self.frames = {
            's': pygame.image.load(static_image),
            'p': pygame.image.load(pressed_image)
        }
        self.index = 's'
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=(pos))
        self.set_text(text)


    # Could've been in __init__ but changing the text is needed for keybind change
    def set_text(self,text):
        # Text
        if text != "None":
            self.text_surf = self.font.render(text,False,'#ffffff')
            self.shadow = self.font.render(text,False,'#7AC7C4')
            self.text_rect = self.text_surf.get_rect(center=(self.rect.center))
            self.shadow_rect = self.shadow.get_rect(center=(self.rect.centerx+3,self.rect.centery+3))


    # To change the button image (for the music button)
    def change_type(self,type):
        self.frames.update({
            's': pygame.image.load(os.path.join('resources', 'menu', 'static', f'{type}.png')),
            'p': pygame.image.load(os.path.join('resources', 'menu', 'pressed', f'{type}.png'))
            })

    
    # Listen for user input/mouse movement
    def listen(self):
        # Get Mouse Pos
        mouse_pos = pygame.mouse.get_pos()
        # Is the Mouse Hovering the button
        mouse_hover = (mouse_pos[0] in range(self.rect.left,self.rect.right) and mouse_pos[1] in range(self.rect.top,self.rect.bottom))
        # Was the mouse pressed
        mouse_press = (pygame.mouse.get_pressed()[0])

        # Change button state upon mouse hover
        if mouse_hover:
            self.index = 'p'
        else:
            self.index = 's'

        # Button click/Button Functions
        if self.name == 'play' and mouse_hover and mouse_press:
            transition(self.screen,self.group)
            settings.onMainMenu = False
            settings.isPlaying = True
        elif self.name == 'settings' and mouse_hover and mouse_press:
            transition(self.screen,self.group)
            settings.onMainMenu = False
            settings.onSettings = True
        elif self.name == 'main-menu' and mouse_hover and mouse_press:
            transition(self.screen,self.group)
            settings.onMainMenu = True
            settings.onPause = False
        elif 'move' in self.name and mouse_hover and mouse_press:
            keybind_change(self.name)
            self.set_text(pygame.key.name(settings.config[self.name.replace('move-', '')]))
        elif 'music' in self.name and mouse_hover and mouse_press:
            sleep(0.25)
            if settings.config['sound'] == "on":
                settings.config['sound'] = "off"
                settings.save_config('config/config.json')
                self.change_type('music-button-off')
                stop_music()
            elif settings.config['sound'] == "off":
                settings.config['sound'] = "on"
                settings.save_config('config/config.json')
                self.change_type('music-button-on')
                play_music()


    # Update Button
    def update(self):
        # If not label, listen for user input/mouse movement
        if self.doListen:
            self.listen()
            self.image = self.frames[self.index]

        # Display/Render the button/label
        self.screen.blit(self.image,self.rect)

        # Display/Render text if there is one
        if self.hasText:
            self.screen.blit(self.shadow,self.shadow_rect)
            self.screen.blit(self.text_surf,self.text_rect)
            


# Made because I don't want to copy-paste this part of the code again and again
def transition(screen,group):
    screen.fill('black')
    sleep(0.25)
    for sprite in group.sprites():
        sprite.kill()


def keybind_change(name):
    checking = True
    while checking:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                settings.config[name.replace('move-', '')] = event.key
                settings.save_config("config/config.json")
                checking = False
                return