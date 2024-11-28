import pygame
class PlaySound:

    def playWinSound(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Victory.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
