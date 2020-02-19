#!/usr/bin/env python3

#Python script for controlling a cpu fan on an Orange Pi Zero Plus.
#The program uses os- and sys-libraries and parts of time and pyA20 libraries.

#The first line tells the operating system to handle this file as a python program.

#Jyri Valta 2019

#Import modules os and sys for using with operating system functions:

import os
import sys

#Import parts of the following libraries:
#From time-library import sleep function so we can make the program sleep for a specified time:

from time import sleep

#From pyA20-library import gpio function for control of the gpio pins.

from pyA20.gpio import gpio

#From pyA20.gpio library import port function for controlling the pins via port names.

from pyA20.gpio import port

#First check that we are running the program with root privileges:

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

#Set the constants used by the program:

led = port.STATUS_LED	#Set STATUS_LED as port led.
fan = port.PA7	#Set PA7 as the fan port.
limit = 45.0	#Set tempreture treshold to 45 degrees celcius.

gpio.init()	#Initialize the gpio pins.
gpio.setcfg(led, gpio.OUTPUT)	#Set the led port as output.
gpio.setcfg(fan, gpio.OUTPUT)	#And the fan port as output.

#Create an endless loop by presenting a while loop that is always true.

while True:

#Open file /etc/armbianmonitor/datasources/soctemp
#that contains the cpu temperature:
    with open('/etc/armbianmonitor/datasources/soctemp', 'r') as txt:
        cputemp = float(txt.read())	#And read it into a variable called cputemp.
        if int(cputemp) > limit:	#If the variable is greater than the treshold:
            gpio.output(led, 1)	#Light the red status led
            gpio.output(fan, 1)	#and turn on the fan.
            sleep(30)		#After that wait for 30 seconds.
            continue		#Return to the start of the while loop.
        else:			#If the variable is equal to or smaller than treshold
            gpio.output(led, 0)	#turn red led off
            gpio.output(fan, 0)	#and the fan.
            sleep(2)		#Wait for 2 seconds
        continue		#and return to the start of the while loop.
