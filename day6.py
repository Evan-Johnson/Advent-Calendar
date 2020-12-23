f = open('input6.txt', 'r')

myDict = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}

def addToTotal(myDict, lines):
    values = myDict.values()
    sum = 0
    for items in values:
        if items == lines:
            sum += 1
    print(sum)
    return sum

def resetDictionary(myDict):
    myDict["a"] = 0
    myDict["b"] = 0
    myDict["c"] = 0
    myDict["d"] = 0
    myDict["e"] = 0
    myDict["f"] = 0
    myDict["g"] = 0
    myDict["h"] = 0
    myDict["i"] = 0
    myDict["j"] = 0
    myDict["k"] = 0
    myDict["l"] = 0
    myDict["m"] = 0
    myDict["n"] = 0
    myDict["o"] = 0
    myDict["p"] = 0
    myDict["q"] = 0
    myDict["r"] = 0
    myDict["s"] = 0
    myDict["t"] = 0
    myDict["u"] = 0
    myDict["v"] = 0
    myDict["w"] = 0
    myDict["x"] = 0
    myDict["y"] = 0
    myDict["z"] = 0

count = 0
line_count = 0
for lines in f:
    if lines[0] == '\n':
        count += addToTotal(myDict, line_count)
        resetDictionary(myDict)
        line_count = 0
    else:
        line_count += 1
        for i in range(0, len(lines)):
            if lines[i] != '\n':
                myDict[lines[i]] += 1
count += addToTotal(myDict, line_count)

print(count)
