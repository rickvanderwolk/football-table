import RPi.GPIO as GPIO
import threading
import time
import tkinter as tk
import sys
import pygame

blue_sensor_pin = 24
red_sensor_pin = 23

blue_score = 0
red_score = 0

def start_game():
    global blue_score
    global red_score
    global blue_sensor_pin
    global red_sensor_pin
    blue_score = 0
    red_score = 0
    GPIO.add_event_detect(blue_sensor_pin, GPIO.FALLING, callback=blue_sensor_callback, bouncetime=300)
    GPIO.add_event_detect(red_sensor_pin, GPIO.FALLING, callback=red_sensor_callback, bouncetime=300)
    play_sound('sounds/start_game.mp3')

def reset_game_if_needed():
    global blue_score
    global red_score
    global blue_sensor_pin
    global red_sensor_pin
    if blue_score == 10 or red_score == 10:
        GPIO.remove_event_detect(blue_sensor_pin)
        GPIO.remove_event_detect(red_sensor_pin)
        if (blue_score == 10 and red_score == 0) or (red_score == 10 and blue_score == 0):
           print('game over, crawl alarm!')
           play_sound('sounds/crawl_alarm.mp3')
           time.sleep(60)
        else:
           print('game over')
           play_sound('sounds/game_over.mp3')
           time.sleep(15)
        start_game()

def play_sound(sound):
    sound = str(sound)
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()

def update_score(team, score):
    global blue_score
    global red_score
    if team == 'blue':
        if (blue_score != score):
            play_sound('sounds/goal.mp3')
        blue_score = score
    elif team == 'red':
        if (blue_score != score):
            play_sound('sounds/goal.mp3')
        red_score = score
    print(team, 'team score:', score)
    reset_game_if_needed()

def blue_sensor_callback(channel):
    update_score('blue', blue_score+1)

def red_sensor_callback(channel):
    update_score('red', red_score+1)

def update_ui():
    label = tk.Label(ui, text='Red: {}  Blue: {}'.format(red_score, blue_score), fg = 'white')
    label.pack()
    while True:
        label.config(font=('Arial', 172))
        label.config(text='{} - {}'.format(red_score, blue_score))
        label.place(relx=0.5, rely=0.5, anchor='center')
        time.sleep(0.1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(blue_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(red_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

start_game()

ui = tk.Tk()
# ui.attributes('-fullscreen', True)
screen_width = ui.winfo_screenwidth()
screen_height = ui.winfo_screenheight()
frame_width = screen_width / 2
ui.geometry(f'{screen_width}x{screen_height}+0+0')
left_frame = tk.Frame(ui, bg = 'red', width=frame_width, height=screen_height)
right_frame = tk.Frame(ui, bg = 'blue', width=frame_width, height=screen_height)
left_frame.place(x=0, y=0, width = frame_width, height = screen_height)
right_frame.place(x=frame_width, y=0, width = frame_width, height = screen_height)
ui_thread = threading.Thread(target=update_ui)
ui_thread.start()
ui.mainloop()
