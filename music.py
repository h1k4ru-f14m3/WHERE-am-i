import pygame
import settings


def play_music():
    # If music is already playing or it isn't turned on, return
    if pygame.mixer.get_busy() or settings.config['sound'] == "off":
        return
    
    # Play the background music indefinitely
    bg_music = pygame.mixer.Sound('music/title-theme.mp3')
    bg_music.play(-1)


def stop_music():
    # If music isn't on, just return because it's no use
    if not pygame.mixer.get_busy():
        return
    
    # Stop the music
    pygame.mixer.stop()

    
        