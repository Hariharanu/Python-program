n=input().split(" ")
n=list(map(int,n))
m=input().split(" ")[:n[0]]
m=list(map(int,m))
for i in range(1,n[1]+1):
	s=m[n[0]-1]
	for j in range(n[0]-1,0,-1):
		m[j]=m[j-1]
	m[0]=s
m=list(map(str,m))
print(" ".join(m))
