import time
import random

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
    print("'The chanting has become defening.'")
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
    time.sleep(3)
    if (stance!="block" and stance!="sweep" and stance!="attack"):
        print("That isn't possible right now!")
        time.sleep(2)
        fight()
    else:
        time.sleep(2)
        fate()

def fate():
    global stance
    global player_health
    global enemy_health
    opponent=random.choice(["block","sweep","attack"])
    if (stance=="block" and opponent=="block"):
        print("At the last moment the both of you raise your shields")
        time.sleep(3)
        print("The two of you slam into each other with incredible force as the crowd cheers")
        time.sleep(3)
        print("Miraculously both of you are unharmed")
        time.sleep(2.5)
    elif (stance=="block" and opponent=="sweep"):
        player_health-=1
        print("You raise your shield to defend yourself")
        time.sleep(3)
        print("But your opponent slides at the last second")
        time.sleep(3)
        print("kicking your legs out from under you")
        time.sleep(3)
        print("You hit the ground hard enough that your vision blurs")
        time.sleep(3)
        print("health -1")
    elif (stance=="block" and opponent=="attack"):
        enemy_health-=1
        print("You raise your shield just in time to deflect your opponent's blow")
        time.sleep(3)
        print("You counter attack and manage a grazing blow against your enemy")
        time.sleep(3)
        print("enemy health -1")
    elif (stance=="sweep" and opponent=="block"):
        enemy_health-=1
        print("Your opponent raises his shield in an attempt to ram you")
        time.sleep(3)
        print("You duck underneath and grab your opponent")
        time.sleep(3)
        print("With all your strength you flip him over you")
        time.sleep(3)
        print("He lands with a thud as the crowd erupts")
        time.sleep(2.5)
        print("enemy health -1")
    elif (stance=="sweep" and opponent=="sweep"):
        print("placeholder")
    elif (stance=="sweep" and opponent=="attack"):
        player_health-=1
        print("ouch")
    elif (stance=="attack" and opponent=="block"):
        player_health-=1
        print("ouch")
    elif (stance=="attack" and opponent=="sweep"):
        enemy_health-=1
        print("gotcha")
    elif (stance=="attack" and opponent=="attack"):
        print("placeholder")
    if (player_health==0):
        defeat()
    elif (enemy_health==0):
        defeat()
    else:
        fight()

def defeat():
    print("You dead")

def victory():
    print("You not dead")

intro()