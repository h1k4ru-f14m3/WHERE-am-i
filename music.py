import pygame
import settings


# def play_main(track):
#     if not pygame.mixer.get_busy():
#         music = pygame.mixer.Sound(track)
#         music.play(-1)


# def play_bg(track1):
#     if not pygame.mixer.get_busy():
#         music1 = pygame.mixer.Sound(track1)
#         music1.play(-1)


def play_music():
    if pygame.mixer.get_busy() or settings.config['sound'] == "off":
        return
    
    menu_music = pygame.mixer.Sound('music/title-theme.mp3')
    bg_music = pygame.mixer.Sound('music/able-sisters.mp3')

    if settings.onMainMenu or settings.onSettings:
        menu_music.play(-1)
    elif settings.onPause or settings.isPlaying:
        bg_music.play(-1)


def stop_music():
    if not pygame.mixer.get_busy():
        return
    
    pygame.mixer.stop()

    
        