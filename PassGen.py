import random
#----------------------------------------
#
#----------------------------------------

#----------------------------------------
#Functions
#----------------------------------------
def dimArrays():
    #25 chars
    alphaLower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    #25 chars
    alphaUpper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z"]
    #16 chars
    alphaChar = ["!","@","#","$","%","^","&","*","(",")","<",">","?",":",";","_"]

    return alphaLower, alphaUpper,alphaChar

def phase1Print(p1AL,p1AU,p1AC):
    #Testing print, length of arrays
    print("Testing Phase 1: Array Lengths:","aL:", len(p1AL),"aU:", len(p1AU),"aC:", len(p1AC),"end phase 1")

def phase2Print(p2AL,p2AU,p2AC):
    #Testing print, random numbers within array length
    print("Testing Phase 2: Array Random Numbers.","aL: ", random.randint(0, len(p2AL)-1),"aU: ", random.randint(0, len(p2AU)-1),"aC: ", random.randint(0, len(p2AC)-1),"end phase 2")

def userInput():
    print("Getting User Input")
    lengthPWord = input("Length of the password? ")

    try:
        int(lengthPWord)
    except ValueError:
        varIsNumber = False
        print("This is not a valid number!")
        quit()

    alphaLowerUse = input("Use lowercase, 1 for yes, 0 for no?")
    alphaUpperUse = input("Use uppercase, 1 for yes, 0 for no?")
    alphaSpecialUse = input("Use special characters, 1 for yes, 0 for no?")

    userInput = [lengthPWord,alphaLowerUse,alphaUpperUse,alphaSpecialUse]
    print("end User Input")

    return userInput

def userChoises(arr):
    aLUse = arr[1]
    aUUse = arr[2]
    aSUse = arr[3]

    if aLUse == "1" and aUUse == "0" and aSUse == "0":
        lowerOnly(arrUI[0])

    elif aLUse == "0" and aUUse == "1" and aSUse == "0":
        UpperOnly(arrUI[0])

    elif aLUse == "0" and aUUse == "0" and aSUse == "1":
        specialOnly(arrUI[0])

    elif aLUse == "0" and aUUse == "0" and aSUse == "0":
        print("Your Password is:")
        print("Hard to make a password if you dont want to use any characters")

    elif aLUse == "1" and aUUse == "1" and aSUse == "0":
        lowerAndUpper(arrUI[0])

    elif aLUse == "1" and aUUse == "0" and aSUse == "1":
        lowerAndSpecial(arrUI[0])

    elif aLUse == "1" and aUUse == "1" and aSUse == "1":
        allSelected(arrUI[0])

    else:
        gotchaBro()
        




#----------------------------------------
#Calculate password length requirements
#----------------------------------------

def lowerOnly(PWLen):

    PW = ""
    x = int(PWLen)

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(x):
            PW += aL[random.randint(0, len(aL)-1)]
    
    #Shuffle Strings
    str_toShuffle = list(PW)
    random.shuffle(str_toShuffle)
    print(''.join(str_toShuffle))

def lowerAndUpper(PWLen):
    PW = ""
    x = int(PWLen)

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(round(x/2)):
            PW += aL[random.randint(0, len(aL)-1)]

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(round(x/2)):
            PW += aU[random.randint(0, len(aU)-1)]

    print(PW)
    #Shuffle Strings
    str_toShuffle = list(PW)
    random.shuffle(str_toShuffle)
    print(''.join(str_toShuffle))

def lowerAndSpecial(PWLen):
    PW = ""
    x = int(PWLen)

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(round(x/2)):
            PW += aL[random.randint(0, len(aL)-1)]

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(round(x/2)):
            PW += aC[random.randint(0, len(aC)-1)]

    print(PW)
    #Shuffle Strings
    str_toShuffle = list(PW)
    random.shuffle(str_toShuffle)
    print(''.join(str_toShuffle))

def UpperOnly(PWLen):

    PW = ""
    x = int(PWLen)

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(x):
            PW += aU[random.randint(0, len(aU)-1)]
    
    #Shuffle Strings
    str_toShuffle = list(PW)
    random.shuffle(str_toShuffle)
    print(''.join(str_toShuffle))

def specialOnly(PWLen):

    PW = ""
    x = int(PWLen)

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(x):
            PW += aC[random.randint(0, len(aC)-1)]
    
    #Shuffle Strings
    str_toShuffle = list(PW)
    random.shuffle(str_toShuffle)
    print(''.join(str_toShuffle))

def upperAndSpecial(PWLen):
    PW = ""
    x = int(PWLen)

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(round(x/2)):
            PW += aU[random.randint(0, len(aU)-1)]

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(round(x/2)):
            PW += aC[random.randint(0, len(aC)-1)]

    print(PW)
    #Shuffle Strings
    str_toShuffle = list(PW)
    random.shuffle(str_toShuffle)
    print(''.join(str_toShuffle))

def gotchaBro():
    print("Your Password is:")
    print("Yes, I did parse your inputs")

def allSelected(PWLen):
    PW = ""
    x = int(PWLen)

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(round(x/3)):
            PW += aU[random.randint(0, len(aU)-1)]

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(round(x/3)):
            PW += aC[random.randint(0, len(aC)-1)]

    if x < 1:
        print("Too small")
    elif x >= 1:
        for i in range(round(x/3)):
            PW += aL[random.randint(0, len(aL)-1)]

    print(PW)
    #Shuffle Strings
    str_toShuffle = list(PW)
    random.shuffle(str_toShuffle)
    print(''.join(str_toShuffle))
#----------------------------------------
#Calls
#----------------------------------------
#Create arrays
aL,aU,aC = dimArrays()

#Phase 1
#phase1Print(aL,aU,aC)

#Phase 2
#phase2Print(aL,aU,aC)

#Assign User Input To Array
arrUI = userInput()

#Phase 3
userChoises(arrUI)