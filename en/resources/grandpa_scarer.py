import RPi.GPIO as GPIO
import time
import pygame
import random

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)  
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)
p = GPIO.PWM(11, 50)
p.start(0)

def waitButton():
    GPIO.wait_for_edge(18, GPIO.RISING)  # Wait for the button to be pressed

def sound():
    sounds = [
        "Female_Scream_Horror-NeoPhyTe-138499973.mp3",
        "Monster_Gigante-Doberman-1334685792.mp3",
        "Scary Scream-SoundBible.com-1115384336.mp3",
        "Sick_Villain-Peter_De_Lang-1465872262.mp3",
    ]

    choice = random.choice(sounds)
    
    pygame.mixer.init()
    pygame.mixer.music.load(choice)
    pygame.mixer.music.play()

    # Wait for the sound to finish
    while pygame.mixer.music.get_busy():
        continue
    time.sleep(0.3)

# Main program section
while True:  # Forever loop (until you hit ctrl+c)
    try:
        waitButton()           # Wait until the button is pushed
        p.ChangeDutyCycle(3)   # Changes the pulse width to 3 (so moves the servo)
        time.sleep(0.1)        # Allow the servo to move
        sound()                # Play a sound file
        time.sleep(2)          # Wait for 2 seconds to allow you to release the button
        waitButton()           # Wait until the button is pushed
        p.ChangeDutyCycle(12)  # Changes the pulse width to 12 (so moves the servo back)
        time.sleep(1)          # Allow the servo to move and start program again
    except(KeyboardInterrupt):  
        p.stop()               # At the end of the program, stop the PWM
        GPIO.cleanup()         # Resets the GPIO pins back to defaults
