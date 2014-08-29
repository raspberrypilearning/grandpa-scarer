##Step 0: Setup your Raspberry Pi
You will need to set up your Raspberry Pi to take part in this activity. [See the Raspberry Pi Quick Start Guide here](http://www.raspberrypi.org/quick-start-guide) to get you up and running.

Then to make sure everything is up to date, open an lxterminal and enter
```sudo apt-get update && upgrade```

##Step 1: Making the box enclosure
![Box](images/drawing.jpg)
To make the box, we recommend lasercutting it out of 3mm plywood. The simplest way to do this is find a local makerspace/hackspace with a lasercutter and politely ask them if they can help.
Many schools now also have small lasercutters so you may be able to ask your Design and Technology department if they can help.
The required file ready to cut can be found here -
The settings required are as follows
- **Black** - Cutting completely through power
- **Red** - Score power, should only leave faint lines

The required cutting area is 550mm x 400mm. If your lasercutter bed is smaller than that then open the file in the program like Inkscape or Adobe Illustrator and split it into 2 sheets.

**As every lasercutter is different and lasers are dangerous, please only operate a lasercutter if you are trained to use that specific lasercutter and its owner is happy with you doing so.**

1. Lasercut the box using the settings above.
![Lasering](images/Lasering.jpg)
2. Use a hot-glue gun to glue all the pieces of the box together. You may need someone else to help you to hold the box together as you glue it. Don't be worried if it goes everywhere, no one sees the inside of the box!
![BoxGlue](images/BoxGlue1.jpg)
3. Grab your hinges and hot glue them on the opposite side of the servo mount on the top side of the box.
![Hinges](images/Hinges1.jpg)
![Hinges](images/Hinges2.jpg)  

##Step 2: Using a servo
![Servo](images/Servo.jpg)
Servos are small motors with control circuitery embedded that can turn up to 180 degrees.
You control the servo by turning one of the GPIO pins on and off at an incredibly fast rate. The length of the pulses (also known as pulse width) is what controls which direct the servo is pointing in.
These signals are called PWM (Pulse Width Modulation) and allows you to do all maner of things from dimming LEDs to driving motors slower than normal.
The Raspberry Pi as standard does not support generating these PWM signals as it does not have a dedicated clock system to do it. For this project we are using software generated PWM signals. The drawback of this though is the signals won't be perfect so the servo may jiggle back and forth a bit.

####Using a servo with RPi.GPIO
We will be using a servo for the latch that holds the panel closed.
RPi.GPIO allows for really easy software PWM to be added to your Python programs.
``` python
#Setup libraries and overall settings
import RPi.GPIO as GPIO  #Imports the standard Raspberry Pi GPIO library
from time import sleep   #Imports sleep (aka wait or pause) into the program
GPIO.setmode(GPIO.BOARD) #Sets the pin numbering system to using the physical layout

#Setup pin 11 for PWM
GPIO.setup(11,GPIO.OUT)  #Sets up pin 11 to an output (instead of an input)
p = GPIO.PWM(11, 50)     #Sets up pin 11 as a PWM pin
p.start(0)               #Starts running PWM on the pin and sets it to 0

#Move the servo back and forth
p.ChangeDutyCycle(3)     #Changes the pulse width to 3 (so moves the servo)
sleep(1)                 #Wait 1 second
p.ChangeDutyCycle(12)    #Changes the pulse width to 12 (so moves the servo)
sleep(1)

#Cleanup everything
p.stop()                 #At the end of the program, stop the PWM
GPIO.cleanup()           #Resets the GPIO pins back to defaults
```


##Step 3: Wiring the button and LED up

##Step 4: Playing sounds

##Step 5: Assembly

##Step 6: Code

##Step 7: Scare a grandpa
