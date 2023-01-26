import sys
import pygame

# Initialiseer pygame
pygame.init()

# Hide the cursor
# pygame.mouse.set_visible(False)

# Stel de schermresolutie in
screen_width = 1920
screen_height = 1080
# @todo enable fullscreen on production
#screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
screen = pygame.display.set_mode((screen_width, screen_height))

# Stel de scores in
team_blue_score = int(sys.argv[1])
team_red_score = int(sys.argv[2])

# Zet de achtergrondkleur op wit
screen.fill((255, 255, 255))

# Maak een blauw vlak voor team red
red_rect = pygame.Rect(0, 0, screen_width / 2, screen_height)
pygame.draw.rect(screen, (255, 0, 0), red_rect)

# Maak een rood vlak voor team blue
blue_rect = pygame.Rect(screen_width / 2, 0, screen_width / 2, screen_height)
pygame.draw.rect(screen, (0, 0, 255), blue_rect)

# Maak twee tekstvakken om de scores weer te geven
font = pygame.font.Font(None, 500)
text_red = font.render(str(team_red_score), 1, (255, 255, 255))
text_blue = font.render(str(team_blue_score), 1, (255, 255, 255))

# Blit de tekst op het scherm
screen.blit(text_red, (screen_width / 4 - text_blue.get_width() / 2, screen_height / 2 - text_blue.get_height() / 2))
screen.blit(text_blue, (3 * screen_width / 4 - text_red.get_width() / 2, screen_height / 2 - text_red.get_height() / 2))

# Toon het scherm
pygame.display.flip()

# Wacht tot de gebruiker het scherm sluit
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
