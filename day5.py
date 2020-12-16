
f = open("input5.txt", 'r')

def find_row(input, left, right):
    temp = (left + right) / 2
    if input[0] == 'F':
        if right - left < 2:
            return left
        else:
            return find_row(input[1:], left, int(temp))
    elif input[0] == 'B':
        if right - left < 2:
            return right
        else:
            return find_row(input[1:], int(temp) + 1, right)
    else:
        print("this shouldn't happen")
        return 0
    
def find_col(input, left, right):
    temp = int((left + right) / 2)
    if (input[0] == 'F') or (input[0] == 'B'):
        return find_col(input[1:], left, right)
    elif input[0] == 'L':
        if right - left < 2:
            return left
        else:
            return find_col(input[1:], left, temp)
    elif input[0] == 'R':
        if right - left < 2:
            return right
        else:
            return find_col(input[1:], temp + 1, right)
    else:
        print("this shouldn't happen either")
        return 0

#max_ID = 0
theList = []

for line in f:
    x = find_row(line, 0, 127)
    y = find_col(line, 0, 7)
    seat_ID = x * 8 + y
    theList.append(seat_ID)
    
    #if seat_ID > max_ID:
    #   max_ID = seat_ID

#print(max_ID)

theList.sort()
for i in range(17, 1015):
    found = False
    for items in theList:
        if i == items:
            found = True
    if found == False:
        print(i)
