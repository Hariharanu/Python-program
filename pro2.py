r,m=[],[]
n=list(map(int,input().split(" ")))
m=n[0]
m=str(m)
for i in range (0,len(m)):
    if i!=n[1]-1:
        r.append(m[i])
r.sort(reverse=True)
print("".join(r))
