import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('mothers-day.mp3')
pygame.mixer.music.play()
image = pygame.image.load('mothers-day.png')
window.blit(image,(150,130))
pygame.display.update()
sleep(20)