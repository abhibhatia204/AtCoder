a , b ,c = list(map(int,input().split()))
t = []
if c > b :
    if b < a and a< c:
        print("No")
    else:
        print("Yes")
else:
    if b <=24:
        for i in range(b,25):
            t.append(i)
        for j in range(0,c+1):
            t.append(j)
    if a in t:
        print("No")
    else:
        print("Yes")  