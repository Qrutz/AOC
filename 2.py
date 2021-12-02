list1 = []
with open('2.txt', 'r') as f:
    for line in f.readlines():
        line = line.split()
        list1.append((line))


def firstTask(list=list1):
    y = 0
    z = 0

    for i in range(len(list)):
        if list[i][0] == 'forward':
            y = y + int(list[i][1])
            print('forward', list[i][1])
        elif list[i][0] == 'down':
            z = z + int(list[i][1])
            print('depth', list[i][1])
        elif list[i][0] == 'up':
            z = z - int(list[i][1])
            print('up', list[i][1])
    print(y*z)


def secondTask(list=list1):
    horiPos = 0
    depth = 0
    aim = 0

    for i in range(len(list)):
        if list[i][0] == 'forward':
            horiPos = horiPos + int(list[i][1])
            depth = depth + (int(list[i][1]) * aim)
            print("add ", list[i][1], 'to your horizontal position, a total of ',
                  horiPos, 'because your aim is ', aim, 'your depth increases by', depth)
        elif list[i][0] == 'down':
            aim = aim + int(list[i][1])
            print("add ", list[i][1],
                  'to your aim resulting in a value of ', aim)
        elif list[i][0] == 'up':
            aim = aim - int(list[i][1])
    print(horiPos*depth)
