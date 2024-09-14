a , b , c = list(map(str,input().split()))
if a==b==c :
    print("B")
else:
    if a==b and b!=c:
        print("C")
    else:
        print("A")