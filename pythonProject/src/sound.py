import pygame
class PlaySound:

    @staticmethod
    def playWinSound(): #Sound for battle victory
        pygame.mixer.init() #initialise pygame sound
        pygame.mixer.music.load('audio/Victory.wav') #Specifies which file to use
        pygame.mixer.music.play() #play file
        while pygame.mixer.music.get_busy(): #wait until sound finishes before continuing
            pass

    @staticmethod
    def playPunchSound(): #Sound for punch, used in battles
        pygame.mixer.init() #initialise pygame sound
        pygame.mixer.music.load('audio/Punch.wav') #Specifies which file to use
        pygame.mixer.music.play() #play file
        while pygame.mixer.music.get_busy(): #wait until sound finishes before continuing
            pass

    @staticmethod
    def playxSound(): #Battle start sound
        pygame.mixer.init() #initialise pygame sound
        pygame.mixer.music.load('audio/deltarunebattle.wav') #Specifies which file to use
        pygame.mixer.music.play() #play file
        while pygame.mixer.music.get_busy(): #wait until sound finishes before continuing
            pass

PlaySound.playPunchSound() #test