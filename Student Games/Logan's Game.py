#learning how to combine an integer and a string
def easyfuntion():
    print("{} is a string, but {} is an integer".format("logan",3))
    return

#learn how to combine two user inputs into a sentence
def areYouQualified():
    N = raw_input("Hello what is you name?")
    A = raw_input("Hi " + N + " can you now tell me your age?")
    print("welcome " + N + " your age is " + A + " years old you are qualified to join this group")
    return

#buggy code.  we are trying to do a string and integer comparison
def areYouQualified2_dataTypeBug():
    N = raw_input("Hello what is you name?")
    A = raw_input("Hi " + N + " can you now tell me your age?")
    if (A < 9):
        print("Sorry you are too young you have to be older than nine and you are " + A + " this game has explicit material this is for your own safety.")
    else:
        print("welcome " + N + " your age is " + A + " years old you are qualified to join this group")
    return

#corrected code.  learning about conditionals, data type conversion and combining strings and integers
def areYouQualified2():
    N = raw_input("Hello what is you name?")
    A = raw_input("Hi " + N + " can you now tell me your age?")
    A = int(A)
    if (A < 9):
        print("Sorry you are too young you have to be older than nine and you are {} this game has explicit material this is for your own safety.".format(A))
    else:
        print("welcome " + N + " your age is {} years old you are qualified to join this game".format(A))
    return

areYouQualified2()
