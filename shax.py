a = int(input('Введите сторону a'))
b = int(input('Введите сторону b'))

list = []
x = 1
y = 1

def shax(x, y, a, b):
    global list
    if 0 < x <= a and 0 < y <= b:
        tryall = 0

        for allb in range(1, b+1):
            if [x, allb] in list:
                tryall += 1


        for alla in range(1, a+1):
            if [alla, y] in list:
                tryall += 1
        if x < y:
            testx = 1
            testy = y - x + 1
        elif x == y:
            testx = 1
            testy = 1
        elif y < x:
            testx = x - y + 1
            testy = 1
        while 0 < testx <= a and 0 < testy <= b:
            testx = testx + 1
            testy = testy + 1
            if [testx, testy] in list:
                tryall += 1
        if (b - y + 1) == x:
            testx = 1
            testy = b
        elif (b - y + 1) > x:
            testx = 1
            testy = b -(b - y + 1) - x   #y+x-1
        elif (b - y + 1) < x:
            testx = x - (b - y + 1) + 1
            testy = b
        while 0 < testx <= a and 0 < testy <= b:
            testx = testx + 1
            testy = testy - 1
            if [testx, testy] in list:
                tryall += 1
        if tryall == 0:
            list.append([x, y])
        if x < a:
            shax(x+1, y, a, b)
        if x < a and y < b:
            shax(x, y + 1, a, b)

shax(x, y, a, b)

print(list)
print('Количество ферзей -',len(list))