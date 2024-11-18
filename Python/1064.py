x_a,y_a,x_b,y_b,x_c,y_c = map(int, input().split())

def distant(a,b,c,d):
    return(((a-c)**2 + (b-d)**2)**(1/2))

dis_lst = [distant(x_a, y_a, x_b, y_b), distant(x_b, y_b, x_c, y_c), distant(x_c, y_c, x_a, y_a)]
if (x_a-x_b)*(y_a-y_c) == (x_a-x_c)*(y_a-y_b):
    print("-1.0")
else:
    print(round((max(dis_lst)-min(dis_lst))*2, 16))