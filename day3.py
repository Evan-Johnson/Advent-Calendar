f = open('input3.txt', 'r')
i = 0
count = 0

for line in f:
    if i % 2 == 0:
        position = int((i / 2) % 31)
        if ((line[position] == '#') and (i % 2 == 0)):
            count += 1
    i += 1

#R1 D1 => 100
#R3 D1 => 276
#R5 D1 => 85
#R7 D1 => 90
#R1 D2 => 37

answer = 100 * 276 * 85 * 90 * 37


print(answer)
f.close()

