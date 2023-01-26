import sys
import pygame

sound = str(sys.argv[1])
print('sound: ')
print(sound)

# Laad het mp3-bestand
pygame.mixer.init()
pygame.mixer.music.load(sound)

# Speel het bestand af
pygame.mixer.music.play()

# Wacht totdat het afspelen is voltooid
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
