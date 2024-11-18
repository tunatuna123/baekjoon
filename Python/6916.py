n = int(input())

def flat():
    print(" * * *")
def side():
    print("*     *")
def left():
    print('*')
def right():
    print('      *')
def empty():
    print()

if n == 0:
    flat()
    side()
    side()
    side()
    empty()
    side()
    side()
    side()
    flat()


elif n == 1:
    empty()
    right()
    right()
    right()
    empty()
    right()
    right()
    right()

elif n == 2:
    flat()
    right()
    right()
    right()
    flat()
    left()
    left()
    left()
    flat()

elif n == 3:
    flat()
    right()
    right()
    right()
    flat()
    right()
    right()
    right()
    flat()

elif n == 4:
    empty()
    side()
    side()
    side()
    flat()
    right()
    right()
    right()

elif n == 5:
    flat()
    left()
    left()
    left()
    flat()
    right()
    right()
    right()
    flat()

elif n == 6:
    flat()
    left()
    left()
    left()
    flat()
    side()
    side()
    side()
    flat()

elif n == 7:
    flat()
    right()
    right()
    right()
    empty()
    right()
    right()
    right()

elif n == 8:
    flat()
    side()
    side()
    side()
    flat()
    side()
    side()
    side()
    flat()

elif n == 9:
    flat()
    side()
    side()
    side()
    flat()
    right()
    right()
    right()
    flat()