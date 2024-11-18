def count_vowels(lst):
    return lst.count("a")+lst.count("e")+lst.count("i")+lst.count("o")+lst.count("u")

while True:
    a = input().lower()
    if a != "#":
        print(count_vowels(a))
    else:
        break