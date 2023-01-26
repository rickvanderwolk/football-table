import RPi.GPIO as GPIO
import threading
import time
import tkinter as tk

blue_sensor_pin = 23
red_sensor_pin = 24

blue_score = 0
red_score = 0

def update_score(team, score):
    global blue_score
    global red_score
    if team == "blue":
        blue_score = score
    elif team == "red":
        red_score = score

def blue_callback(channel):
    update_score("blue", blue_score+1)
    print("Blue team score:", blue_score)

def red_callback(channel):
    update_score("red", red_score+1)
    print("Red team score:", red_score)

def update_ui():
    label = tk.Label(ui, text="Red: {}  Blue: {}".format(red_score, blue_score), fg = "white")
    label.pack()
    while True:
        label.config(text="Red: {}  Blue: {}".format(red_score, blue_score))
        time.sleep(0.1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(blue_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(red_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(blue_sensor_pin, GPIO.FALLING, callback=blue_callback, bouncetime=300)
GPIO.add_event_detect(red_sensor_pin, GPIO.FALLING, callback=red_callback, bouncetime=300)

ui = tk.Tk()
ui.geometry("400x200+0+0")
left_frame = tk.Frame(ui, bg = "red", width=200, height=200)
right_frame = tk.Frame(ui, bg = "blue", width=200, height=200)
left_frame.place(x=0, y=0, width = 200, height =200)
right_frame.place(x=200, y=0, width = 200, height =200)
ui_thread = threading.Thread(target=update_ui)
ui_thread.start()
ui.mainloop()
