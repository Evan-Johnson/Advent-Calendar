f = open('input4.txt', 'r')
count = 0

myDict = {
    "byr": 0,
    "iyr": 0,
    "eyr": 0,
    "hgt": 0,
    "hcl": 0,
    "ecl": 0,
    "pid": 0,
    "cid": 0
}

def validate_passport(myDict):
    values = myDict.values()
    sum = 0
    for item in values:
        if item == 1:
            sum += 1
    print(sum, myDict["cid"])
    if sum > 7:
        return True
    elif ((sum == 7) and (myDict["cid"] == 0)):
        return True
    else:
        return False

def reset_dictionary(myDict):
    myDict["byr"] = 0
    myDict["iyr"] = 0
    myDict["eyr"] = 0
    myDict["hgt"] = 0
    myDict["hcl"] = 0
    myDict["ecl"] = 0
    myDict["pid"] = 0
    myDict["cid"] = 0
        
def validate_category(cat, val, myDict):
    if cat == 'byr':
        if ((len(val) == 4) and (int(val) >= 1920) and (int(val) <= 2002)):
            myDict[cat] += 1
    elif cat == 'iyr':
        if ((len(val) == 4) and (int(val) >= 2010) and (int(val) <= 2020)):
            myDict[cat] += 1
    elif cat == 'eyr':
        if ((len(val) == 4) and (int(val) >= 2020) and (int(val) <= 2030)):
            myDict[cat] += 1
    elif cat == 'hgt':
        if ((val[-1] == 'm') and (val[-2] == 'c')):
            val = val[:-2]
            if((int(val) >= 150) and (int(val) <= 193)):
                myDict[cat] += 1
        elif ((val[-1] == 'n') and (val[-2] == 'i')):
            val = val[:-2]
            if((int(val) >= 59) and (int(val) <= 76)):
                myDict[cat] += 1
    elif cat == 'hcl':
        if ((val[0] == '#') and (len(val) == 7)):
            temp_count = 0
            for i in range(1, len(val)):
                if (((val[i] >= 'a') and (val[i] <= 'f')) or ((int(val[i]) >= 0) and (int(val[i]) <= 9))):
                    temp_count += 1
            if temp_count == 6:
                myDict[cat] += 1
    elif cat == 'ecl':
        if ((val == 'amb') or (val == 'blu') or (val == 'brn') or (val == 'gry') or (val == 'grn') or (val == 'hzl') or (val == 'oth')):
            myDict[cat] += 1
    elif cat == 'pid':
        if ((len(val) == 9) and (val.isnumeric())):
            myDict[cat] += 1
    elif cat == 'cid':
        myDict[cat] += 1
    else:
        print("error in the category")

def read_passport(l, myDict):
    arr = l.split()
    for string in arr:
        new_str = string.split(':')
        validate_category(new_str[0], new_str[1], myDict)

for line in f:
    if line[0] == '\n':
        isValid = validate_passport(myDict)
        if isValid == True:
            count += 1
        reset_dictionary(myDict)
    else:
        read_passport(line, myDict)

isValid = validate_passport(myDict)
if isValid == True:
    count += 1

print(count)



