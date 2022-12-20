coord = []
word_dict = {"A":'1', "B":"2", 'C':'3', 'D':'4', 'E':'5', 'F':'6'}
ans = []

for i in range(36):
    a = input()
    coord.append(int(word_dict[a[0]]+a[1]))
for i in range(35):
    ans.append(abs(coord[i]-coord[i+1]))

if (len(set(coord)) == 36) and (set(ans) == {8, 19, 12, 21}) and (abs(coord[0]-coord[-1]) in [8, 19, 12, 21]):
    print("Valid")
else:
    print("Invalid")