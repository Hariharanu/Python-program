n=int(input())
n1=list(list(input().split(" ")))
n2=input()
c=0
for i in range(0,len(n1)):
	w=str(n1[i])
	r=w.count(n2)
	if r>0:
		c=c+1
print(c)
