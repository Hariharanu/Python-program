n=input().split(" ")
n=list(map(int,n))
m=input().split(" ")
m=list(map(int,m))
if n[1] in m:
    print("Yes")
else:
    print("No")
