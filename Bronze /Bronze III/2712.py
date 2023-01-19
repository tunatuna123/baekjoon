n = int(input())
dic = {'kg':[2.2046, 'lb'], 'lb':[0.4536, 'kg'], 'l':[0.2642, 'g'], 'g':[3.7854, 'l']}
for i in range(n):
    a,b = input().split()
    print("%.4f %s"%(float(a)*(dic[b][0]), dic[b][1]))