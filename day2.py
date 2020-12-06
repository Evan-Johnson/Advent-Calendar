f = open('input2.txt', 'r')

def func(num1, num2, let, pw):
    count = 0
    #This is used for part 1 only (checking if the number of letters is in range)
    #for i in range(0, len(pw)):
    #    if let == pw[i]:
    #        count += 1
    #if ((count >= int(num1)) and (count <= int(num2))):
    #    return True
    #else:
    #    return False

    #Part 2 is asking for an exclusive OR based on the position
    if let == pw[int(num1) - 1]: 
        if let == pw[int(num2) - 1]:
            return False
        else:
            return True
    elif let == pw[int(num2) - 1]: #case second is the right letter but first isnt
        return True
    else: #case letter is not in either spot
        return False



amt = [0, 0]
letter = ""
password = ""
global_count = 0

line = f.readline()
while line != '':
    line = line.rstrip()
    if ((line[1] == '-') and (line[5] == ':')): #single digit for the two numbers
        amt[0] = line[0]
        amt[1] = line[2]
        letter = line[4]
        password = line[7:]
    elif ((line[1]) == '-' and (line[6] == ':')): #double digit second number only
        amt[0] = line[0]
        amt[1] = line[2] + line[3]
        letter = line[5]
        password = line[8:]
    else: #doube digit for both numbers
        amt[0] = line[0] + line[1]
        amt[1] = line[3] + line[4]
        letter = line[6]
        password = line[9:]

    if func(amt[0], amt[1], letter, password) == True:
        global_count += 1
    line = f.readline()

print(global_count)
f.close()
