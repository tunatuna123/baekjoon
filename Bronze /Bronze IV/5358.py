while True:
    try:
        name = input()
        name = name.replace('i', '1')
        name = name.replace("e", "2")
        name = name.replace("E", "3")
        name = name.replace("I", "4")
        name = name.replace('1', 'e')
        name = name.replace("2", 'i')
        name = name.replace("3", 'I')
        name = name.replace("4", 'E')
        print(name)
    except:
        break