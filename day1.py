
f = open("input.txt", "r")

arr = []
for x in f:
    y = int(x)
    arr.append(y)


for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if arr[i] + arr[j] + arr[k] == 2020:
                print(arr[i] * arr[j] * arr[k])

f.close()