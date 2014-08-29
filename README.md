
# Grandpa Scarer

In this project we are going to use a Raspberry Pi to play spooky noises whilst releasing a scary spider from a box onto whoever is underneath.

## Requirements

As well as a Raspberry Pi with an SD card loaded with Raspbian, you'll also need:

### Hardware

- 1 x Push button - we like [this big red one from Proto-PIC](http://proto-pic.co.uk/big-dome-push-button/)
- 1 x Solenoid 5V - [Proto-PIC](http://proto-pic.co.uk/solenoid-5v-small/)
- 1 x Magnet - [Proto-PIC](http://proto-pic.co.uk/magnet-ring-3-16/)
- 1 x Transistor - [Proto-PIC](http://proto-pic.co.uk/common-bjt-transistor-npn-2n3904/)
- 1 x Extra Breadboard power supply - [Proto-PIC](http://proto-pic.co.uk/breadboard-power-supply-5v-3-3v/)
- 1 x Surface Transducer - [Proto-PIC](http://proto-pic.co.uk/surface-transducer-small/)

### Software

- All the software packages that we are going to use are installed in Raspbian by default. Make sure to update your SD card in order to stay current. You can do this with the command: ```sudo apt-get update && sudo apt-get upgrade```

### Extras

- 1 x toy spider
- 1 x meter of elastic string to attach your spider to your box
- A way to attach the box to the ceiling.
- An unsuspecting grandpa

## Steps

1. Making the box enclosure
1. Setting up your Raspberry Pi
1. Setting up a servo
1. Making sounds with a 3.5mm speaker
1. Assembly
1. Code

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

Based on a work at https://github.com/raspberrypilearning/grandpa_scarer
