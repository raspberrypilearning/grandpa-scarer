##Step 0: Setup your Raspberry Pi

##Step 1: Making the box enclosure

##Step 2: Using a servo

##Step 3: Wiring the button and LED up

In order for your grandpa scarer to be activated you will need to hook up a button of some kind - preferably with a long wire attached to it so that you can be far far away when you scare someone. Here is the button that we used:

![](images/button.jpg)

Buttons work on this concept - you have two wires, one connected to ground and the other to one of the GPIO pins on the Pi. You would think that if you set this pin as an input then you'd very easily be able to view the button being pressed. Sadly that is not the case. If we do this then the Pi will not know what state the button is in. This is called a floating input and even things like moving the wires will cause it to change randomly... In order to fix this we need to use the Pi's inbuilt pull up resistors. These are clever little things as they 'pull up' the button into one state. That way when you hit it the Pi will see that it has definitely changed.

Now that you understand the basic principles behind the button's operation lets wire it up. First off you should have two wires connected to two of the pins on your button. The one we used had two clearly marked pins for this however it is not uncommon for buttons (especially the breadboard variety) to have four legs - these are just two sets of two and so make sure that you only wire up one set. TIP: Colour code them. Our wires were around six meters long in order for a maximum scaring distance!

Now that you have two wires connected to your button you will now need to wire it up to your Raspberry Pi

##Step 4: Playing sounds

##Step 5: Assembly

##Step 6: Code

##Step 7: Scare a grandpa
