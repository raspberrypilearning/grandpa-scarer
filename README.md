
# Grandpa Scarer

In this project we are going to use a Raspberry Pi to play spooky noises whilst releasing a scary spider from a box onto whoever is underneath at the press of a button!

![Box](images/finishedBox.jpg)

## Requirements

As well as a Raspberry Pi with an SD card loaded with Raspbian, you'll also need:

### Hardware

- 1 x Push button - we like [this big red one from Proto-PIC](http://proto-pic.co.uk/big-dome-push-button/)
- 1 x Servo - [Proto-PIC](http://proto-pic.co.uk/analogue-9-gram-servo/)
- 1 x Wooden box - [See "Making the box enclosure" section]()
- 1 x Wire set - [Proto-PIC](http://proto-pic.co.uk/hook-up-wire-assortment-solid-core/)
- 1 x Cable ties - [B&Q](http://www.diy.com/nav/fix/electrical/cable-management/cable_ties/B-and-Q-Black-295mm-Cable-Ties-Pack-of-50-12848940?skuId=13359646)
- 1 x Speaker - [PiHut](http://thepihut.com/products/mini-portable-speaker-for-the-raspberry-pi/)
- 2 x Metal hinges - [B&Q](http://www.diy.com/nav/build/doors/door-furniture/door_hinges/-specificproducttype-butt_hinges/B-and-Q-Butt-Hinge-Brass-Plated-9370558?skuId=9671263)
- 1 x 5mm red LED - [Proto-PIC](http://proto-pic.co.uk/led-starter-kit/)
- 1 x 330R resistor - [Proto-PIC](http://proto-pic.co.uk/led-starter-kit/)
- 
#### Optional

- 1 x USB battery pack
- 1 x Wifi adapter

### Software

All the software packages that we are going to use are installed in Raspbian by default. Make sure to update your SD card in order to stay current. You can do this with the command: `sudo apt-get update && sudo apt-get upgrade`


### Extras

- 1 x toy spider
- 1 x meter of elastic string to attach your spider to your box
- A way to attach the box to the ceiling
- An unsuspecting grandpa

## Steps

1. Making the box enclosure
1. Setting up your Raspberry Pi
1. Using a servo
1. Wiring the button and LED up
1. Playing sounds
1. Assembly
1. Code
1. Scare a grandpa!

## Worksheet & included files

- [The worksheet](worksheet.md)
- (Optional) Final version of Python code [grandpa_scarer.py](code/grandpa_scarer.py)
    - Download to your Pi with `wget http://goo.gl/BKd6dJ -O grandpa_scarer.py --no-check-certificate`

## Disclaimer

1. Do not scare people with medical conditions that could be easily be triggered.
2. Make sure that the box is safely and firmly attached to the ceiling. Do not take risks with this as the final product is quite heavy and could be dangerous if it falls on someone. We recommend an adult takes over for this part ;-)
3. Take care when using the machinery described. Always have a qualified adult supervising when using appliances such as laser cutters.

## Community

This project was the work experience task of Matthew Timmons-Brown (The Raspberry Pi Guy) and Andrew Mulholland (gbaman1) who were under the care of Rachel Rayns.

## Licence

Unless otherwise specified, everything in this repository is covered by the following licence:

[![Creative Commons Attribution 4.0 International Licence](http://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

***Grandpa Scarer*** by the [Raspberry Pi Foundation](http://www.raspberrypi.org) is licensed under a [Creative Commons Attribution 4.0 International Licence](http://creativecommons.org/licenses/by-sa/4.0/).

Based on a work at https://github.com/raspberrypilearning/grandpa-scarer
