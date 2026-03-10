import Arma
import pygame

class FuegoPecho(Arma.Arma):
    def __init__(self):
        self.__pechoOn=pygame.image.load('./PechoOn.png')

    def enciende(self,screen):
        screen.blit(self.__pechoOn,(0,0))
        pygame.display.flip()

    def grito(self):
        print('¡¡¡¡¡Fuego de Pecho!!!!')