#this code is meant to integrate hardware into a simple button flip code by
#adding an RGBLED and 3 buttons. This should allow the game to be plyed without
#a monitor
from time import sleep
from random import choice
from gpiozero import RGBLED, Button
from subprocess import check_call
coin=("heads","tails") #creating the 'coin'
led=RGBLED(8,7,1) #creating all of our objects representing the hardware
h=Button(2)
t=Button(3)
pwr_off=Button(14,hold_time=2)
def shutdown(): # this function will shutdown the Pi when called
    check_call(["sudo","poweroff"])
def heads():
    global player #Tried to initialize variable outside of function. Did not
    player="heads"#work. Variable scope different in python?
def tails():
    global player
    player="tails"
def coinflip():
    flip=choice(coin)
    h.when_pressed=heads #Assigning a button to be heads
    t.when_pressed=tails #Assigning a button to be tails
    pwr_off.when_held=shutdown #Assigning a button to shutdown the Pi
    led(0,0,1) #assuming that (0,0,1) is the color code for blue
    while(h.value==0 and t.value==0):
        sleep(0.01) #python does not seem to appreciate null while loops
    if (player==flip):
        led.color=(1,0,0) #assuming that (1,0,0) is the color code for green
        print(flip+"! You won the flip!")
        sleep(2)
        coinflip()
    else:
        led.color=(0,1,0) #assuming that (0,1,0) is the color code for red
        print(flip+". Sorry, you lost the flip.")
        sleep(2)
        coinflip()

coinflip()