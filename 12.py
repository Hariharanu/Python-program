n=list(map(int,input().split(" ")))
m=list(map(int,input().split(" ")))
m.sort(reverse=True)
print(m[n[1]-1])
