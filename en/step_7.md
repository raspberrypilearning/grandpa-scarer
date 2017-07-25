## Playing sounds

One of the key aspects of your grandpa scarer is the loud noise that it will make when you hit the button and your spider springs out. We want the sound to be frightening and *almost* deafening. The Pi doesn't have any built-in speakers, so how do you go about doing this? The answer is to use a small portable speaker that can easily connect to the Pi's 3.5mm audio jack here:

![](images/audio.jpg)

We recommend the Pi Hut's one as it is small, nifty, and powerful. You can easily hold it in place in the enclosure with two cable ties, and it can be charged from the Pi using its accompanying micro USB cable.

Go ahead and plug it into your Raspberry Pi, making sure it is turned on by using the button on the bottom of the speaker. Plug the power lead (micro USB to USB) into the Pi, then plug the 3.5mm audio cable into the jack on the Pi and the jack on the Pi Hut speaker. We have included some scary sounds in the code directory - feel free to add your own and edit the program!

Now let's have a look at the Python code to play those noises:

```python
import time
import pygame
import random

def sound():
    sounds = [
        "Female_Scream_Horror-NeoPhyTe-138499973.mp3",
        "Monster_Gigante-Doberman-1334685792.mp3",
        "Scary Scream-SoundBible.com-1115384336.mp3",
        "Sick_Villain-Peter_De_Lang-1465872262.mp3"
    ]
  
    choice = random.choice(sounds)

    pygame.mixer.init()
    pygame.mixer.music.load(choice)
    pygame.mixer.music.play()
  
    # Wait for the sound to finish
    while pygame.mixer.music.get_busy():
        continue
    time.sleep(0.3)

sound()
```

All the sounds can be found in the [sounds](https://github.com/raspberrypilearning/grandpa-scarer/tree/master/sounds) folder.

To get these on your Raspberry Pi, you can use:

```bash
wget http://goo.gl/SbK5YJ -O Sounds.zip --no-check-certificate
unzip Sounds.zip
```

