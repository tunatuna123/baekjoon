def number_print(a):
    if a == 0:
        print('0000')
        print('0  0')
        print('0  0')
        print('0  0')
        print('0000')

    elif a == 1:
        print('   1')
        print('   1')
        print('   1')
        print('   1')
        print('   1')

    elif a == 2:
        print('2222')
        print('   2')
        print('2222')
        print('2')
        print('2222')

    elif a == 3:
        print('3333')
        print('   3')
        print('3333')
        print('   3')
        print('3333')

    elif a == 4:
        print('4  4')
        print('4  4')
        print('4444')
        print('   4')
        print('   4')

    elif a == 5:
        print('5555')
        print('5')
        print('5555')
        print('   5')
        print('5555')

    elif a == 6:
        print('6666')
        print('6')
        print('6666')
        print('6  6')
        print('6666')

    elif a == 7:
        print('7777')
        print('   7')
        print('   7')
        print('   7')
        print('   7')

    elif a == 8:
        print('8888')
        print('8  8')
        print('8888')
        print('8  8')
        print('8888')
    
    elif a == 9:
        print('9999')
        print('9  9')
        print('9999')
        print('   9')
        print('   9')

n = input()
for i in range(len(n)):
    number_print(int(n[i]))
    if i != len(n)-1:
        print()