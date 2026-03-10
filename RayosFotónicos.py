import Arma
import pygame

class RayosFotónicos(Arma.Arma):
    def __init__(self):
        self.__ojosOn=pygame.image.load('./OjosOn.png')

    def enciende(self,screen):
        screen.blit(self.__ojosOn,(0,0))
        pygame.display.flip()

    def grito(self):
        print('¡¡¡¡¡Rayos Fotónicos!!!!')