count = 1  
while True:
    nasty = 1
    name = []
    word = []
    n = int(input())
    
    if n == 0: 
        break
    for _ in range(n):
        n_w = input()   
        new = n_w.split()   
        name.append(new[0])
        for _ in range(1,n):
            word.append(new[_]) 
    print("Group",count)
    size = n-1  
    for i in range(len(word)): 
        if word[i] == 'N': 
            print(name[size],"was nasty about",name[i//(n-1)])
            nasty = 0
        size -= 1
        if size == -1:
            size = n-1
    if nasty:   
        print("Nobody was nasty")
    print("")
    count += 1