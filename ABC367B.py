x = float(input())
z = x*1
ans = str(z)
if ans[len(ans)-1]!="0":
    print(ans)
else:
    print(ans[0:len(ans)-2])