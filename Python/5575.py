for i in range(3):
    sh,sm,ss,eh,em,es = map(int, input().split())
    start = (sh*3600)+(sm*60)+ss
    end = (eh*3600)+(em*60)+es
    total = end-start
    print(total//3600, (total%3600)//60, (total%3600)%60)