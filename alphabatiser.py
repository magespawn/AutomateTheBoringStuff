#Get user input
def getInput():
    inputString = input("Please provide a string to order")
    return inputString
def convertAlphaList(StringList):
    chrList = []
    for x in StringList:
        chrList.append(ord(x))
    return chrList
def sortTheList(StringList):
    StringList.sort()
    return StringList
def convertListBack(alphList):
    newlist = []
    for x in alphList:
        newlist.append(chr(x))
    #print(newlist)
    i = ''.join(newlist)
    print(i)
    return newlist
StringList = getInput()
StringList = list(StringList)
chrList = convertAlphaList(StringList)
sortedList = sortTheList(chrList)
convertListBack(sortedList)
