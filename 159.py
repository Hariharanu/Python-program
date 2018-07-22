def convertToBinary(n):
	mylist=[]
	while n >0:
		num=n%2
		mylist.append(num)
		n=n//2
	return list(reversed(mylist))
n,m,g=list(map(int,input().split(" "))),[],1
for i in range(0,len(n)):
	g=g*n[i]
z=convertToBinary(g)
print(z.count(1))
