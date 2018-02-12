import time
import random
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17,GPIO.OUT)
#GPIO.setup(27,GPIO.OUT)
#GPIO.setup(22,GPIO.OUT)
#GPIO.setup(10,GPIO.OUT)
#GPIO.setup(9,GPIO.OUT)
#GPIO.setup(11,GPIO.OUT)
#GPIO.setup(18,GPIO.OUT)   #pin 18=Motor

#pwm=GPIO.PWM(18,50)
#pwm.start(3.5)


#GPIO.output(17,GPIO.HIGH)   #player LED1
#GPIO.output(27,GPIO.HIGH)   #player LED2
#GPIO.output(22,GPIO.HIGH)   #player LED3
#GPIO.output(10,GPIO.HIGH)   #enemy LED1
#GPIO.output(9,GPIO.HIGH)    #enemy LED2
#GPIO.output(11,GPIO.HIGH)   #enemy LED3

#def health_display():
#    global player_health
#    global enemy_health
#    if (player_health==2):
#        GPIO.output(22,GPIO.LOW)
#    elif (player_health==1):
#        GPIO.output(27,GPIO.LOW)
#    elif (player_health==0):
#        GGPIO.output(17,GPIO.LOW)
#    elif (enemy_health==2):
#        GPIO.output(11,GPIO.LOW)
#    elif (enemy_health==1):
#        GPIO.output(9,GPIO.LOW)
#    elif (enemy_health==0):
#        GPIO.output(10,GPIO.LOW)

def intro():
    global name
    global player_health
    global enemy_health
    player_health=3
    enemy_health=3
    name=raw_input("What is your name? >")
    time.sleep(3)
    print("Hello "+name)
    time.sleep(3)
    print("It has been many years")
    time.sleep(2)
    print("since I have seen a gladiator")
    time.sleep(2)
    print("As strong as yourself!")
    time.sleep(3)
    print("You have quite the challenge ahead of you now.")
    time.sleep(3)
    print("Good luck!")
    time.sleep(4)
    grand_entrance()

def grand_entrance():
    global name
    print("'The platform you are standing on begins to rise.'")
    time.sleep(3)
    print("'As it rises you bein to hear your name being chanted.'")
    time.sleep(4)
    print("'It grows louder as you rise higher.'")
    time.sleep(3)
    print(name+"!")
    time.sleep(1.5)
    print(name+"!")
    time.sleep(1.5)
    print(name+"!")
    time.sleep(3)
    print("'The platform reaches its apex and you find yourself in a colosseum.'")
    time.sleep(4)
    print("'The chanting has become deafening.'")
    time.sleep(2)
    print(name+"!!!")
    time.sleep(1.5)
    print(name+"!!!")
    time.sleep(1.5)
    print(name+"!!!")
    time.sleep(3)
    print("'Across from you stands another gladiator.'")
    time.sleep(3)
    print("'Without warning your opponent bellows and charges at you!'")
    time.sleep(3)
    fight()

def fight():
    global stance
    print("What will you do?")
    time.sleep(2)
    stance=raw_input(">block >sweep >attack >")
    if (stance!="block" and stance!="sweep" and stance!="attack"):
        print("That isn't possible right now!")
        time.sleep(2)
        fight()
    else:
#        if (stance=="block"):
#            pwm.ChangeDutyCycle(12.5)
#        elif(stance=="sweep"):
#            pwm.ChangeDutyCycle(9.5)
#        else:
#            pwm.ChangeDutyCycle(6.5)
        time.sleep(2)
        fate()

def fate():
    global stance
    global player_health
    global enemy_health
    opponent=random.choice(["block","sweep","attack"])
    if (stance=="block" and opponent=="block"):
        print("Shing!")
        time.sleep(2)
    elif (stance=="block" and opponent=="sweep"):
        player_health-=1
        print("ouch!")
        time.sleep(2)
        print("health -1")
        time.sleep(2)
    elif (stance=="block" and opponent=="attack"):
        enemy_health-=1
        print("Gotcha!")
        time.sleep(2)
        print("enemy health -1")
        time.sleep(2)
    elif (stance=="sweep" and opponent=="block"):
        enemy_health-=1
        print("Gotcha!")
        time.sleep(2)
        print("enemy health -1")
        time.sleep(2)
    elif (stance=="sweep" and opponent=="sweep"):
        print("Shing!")
        time.sleep(2)
    elif (stance=="sweep" and opponent=="attack"):
        player_health-=1
        print("Ouch!")
        time.sleep(2)
        print("health -1")
        time.sleep(2)
    elif (stance=="attack" and opponent=="block"):
        player_health-=1
        print("Ouch!")
        time.sleep(3)
        print("health -1")
        time.sleep(2)
    elif (stance=="attack" and opponent=="sweep"):
        enemy_health-=1
        print("Gotcha!")
        time.sleep(2)
        print("enemy health -1")
        time.sleep(2)
    elif (stance=="attack" and opponent=="attack"):
        print("Shing!")
        time.sleep(3)
#    health_display()
    if (player_health==0):
        defeat()
    elif (enemy_health==0):
        victory()
    else:
        print("You and your opponent reset, weapons drawn, before they charge again")
        time.sleep(3)
        fight()

def defeat():
    global name
    global enemy_health
#    pwm.ChangeDutyCycle(15.5)
    print("Game Over")
    time.sleep(1.5)
    print("You have died. Your enemy had {} health left".format(enemy_health))

def victory():
    global name
    global player_health
#    pwm.ChangeDutyCycle(18.5)
    print("Congradulations {}! You have slain you enemy. You had {} health left".format(name,player_health))

intro()
# GPIO.cleanup()