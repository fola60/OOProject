import pygame
class PlaySound:

    @staticmethod
    def playWinSound():
        pygame.mixer.init()
        pygame.mixer.music.load('audio/Victory.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

    @staticmethod
    def playPunchSound():
        pygame.mixer.init()
        pygame.mixer.music.load('audio/Punch.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

    @staticmethod
    def playxSound():
        pygame.mixer.init()
        pygame.mixer.music.load('audio/deltarunebattle.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

PlaySound.playPunchSound()