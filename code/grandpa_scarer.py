import RPi.GPIO as GPIO  #Imports the standard Raspberry Pi GPIO library
import time              #Imports sleep (aka wait or pause) into the program
import pygame            #Imports pygame to play the sounds
import random            #Imports random to pick a random sound

GPIO.setmode(GPIO.BOARD) #Sets the pin numbering system to using the physical layout

GPIO.setup(11, GPIO.OUT) #Sets up pin 11 to an output (instead of an input)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Sets up pin 18 to an output and enabled the pull up resistor
p = GPIO.PWM(11, 50)     #Sets up pin 11 as a PWM pin
p.start(0)	             #Starts running PWM on the pin and sets it to 0

def waitButton():
  GPIO.wait_for_edge(18, GPIO.RISING)  #Waits for the button to be pressed

def sound():
  # A list full of our sound files
  sounds = ["Female_Scream_Horror-NeoPhyTe-138499973.mp3", "Monster_Gigante-Doberman-1334685792.mp3", "Scary Scream-SoundBible.com-1115384336.mp3", "Sick_Villain-Peter_De_Lang-1465872262.mp3"]
  # Picks a random sound
  choice = random.choice(sounds)
  # Initializes the sound and plays through speaker
  pygame.mixer.init()
  pygame.mixer.music.load(choice)
  pygame.mixer.music.play()
  #Wait till the sound is finshed
  while pygame.mixer.music.get_busy() == True:
      continue
  time.sleep(0.3)

#Main program section
while True:  #Forever loop (until you hit ctrl+c)
  try:
    waitButton()           #Wait until the button is pushed
    p.ChangeDutyCycle(3)   #Changes the pulse width to 3 (so moves the servo)
    time.sleep(0.1)        #Allow the servo to move
    sound()                #Play a sound file
    time.sleep(2)          #Wait for 2 seconds to allow you to release the button
    waitButton()           #Wait until the button is pushed
    p.ChangeDutyCycle(12)  #Changes the pulse width to 12 (so moves the servo back)
    time.sleep(1)          #Allow the servo to move and start program again
  except(KeyboardInterrupt):
    p.stop()               #At the end of the program, stop the PWM
    GPIO.cleanup()         #Resets the GPIO pins back to defaults
