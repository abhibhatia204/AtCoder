n , m = list(map(int,input().split()))
x = set()
for i in range(m):
    cout = 0
    a, b = list(map(str,input().split()))
    n = list(x)
    if b=="F":
        print("No")
    if b =="M":
        for j in range(len(n)):
            if a==n[j]:
                cout +=1
        if cout==0:
            print("Yes")
            x.add(a)
        else:
            print("No")

        
    