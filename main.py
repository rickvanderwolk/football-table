import RPi.GPIO as GPIO
import subprocess
import time

# Stel de GPIO-pin mode in op BCM (Broadcom SOC channel)
GPIO.setmode(GPIO.BCM)

# Stel de pins in die verbonden zijn met de beam break sensoren in als ingang
sensor1_pin = 23
sensor2_pin = 24
GPIO.setup(sensor1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialiseer de scores op 0
score1 = 0
score2 = 0

# Bewaar de vorige waarden van de pinnen
prev_input1 = 1
prev_input2 = 1

def update_screen():
    global display_subprocess
    if 'display_subprocess' in globals():
        display_subprocess.kill()
    arguments = [str(score1), str(score2)]
    display_subprocess = subprocess.Popen(['python', 'ui.py', str(score1), str(score2)])

def play_sound(sound):
    global sound_subprocess
    if 'sound_subprocess' in globals():
      sound_subprocess.kill()
    sound_subprocess = subprocess.Popen(['python', 'sound.py', sound])

def start_game():
    global score1
    global score2
    score1 = 0
    score2 = 0
    update_screen()
    play_sound('sounds/start_game.mp3')

def reset_game_if_needed():
    global score1
    global score2
    # Reset game after one of the teams reaches a score of 10
    if score1 == 10 or score2 == 10:
        if (score1 == 10 and score2 == 0) or (score2 == 10 and score1 == 0):
           play_sound('sounds/crawl_alarm.mp3')
           time.sleep(60)
        else:
           play_sound('sounds/game_over.mp3')
           time.sleep(15)
        start_game()

# Start game
start_game()

# Maak een infinite loop om de sensoren te lezen
while True:
     ## Lees de huidige waarden van de pinnen
     input1 = GPIO.input(sensor1_pin)
     input2 = GPIO.input(sensor2_pin)

     # Als er een verandering is in de waarde van een van de pinnen
     if ((not prev_input1 and input1) or (not prev_input2 and input2)):
         # Als pin1 een verandering heeft, verhoog de score voor pin1
         if (not prev_input1 and input1):
             score1 += 1
             print("Pin 1: Score opgehoogd naar {}".format(score1))
             play_sound('sounds/goal.mp3')
             update_screen()
             reset_game_if_needed()
         # Als pin2 een verandering heeft, verhoog de score voor pin2
         if (not prev_input2 and input2):
             score2 += 1
             print("Pin 2: Score opgehoogd naar {}".format(score2))
             play_sound('sounds/goal.mp3')
             update_screen()
             reset_game_if_needed()

     # Bewaar de huidige waarden voor de volgende iteratie
     prev_input1 = input1
     prev_input2 = input2

# Vergeet niet om de GPIO-pins op te ruimen als je het script stopt
GPIO.cleanup()
