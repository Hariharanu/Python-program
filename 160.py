def convertToBinary(n):
	mylist=[]
	while n >0:
		num=n%2
		mylist.append(num)
		n=n//2
	return list(reversed(mylist))
n,m,g=list(map(int,input().split(" "))),[],1
num=n[0] | n[1]
z=convertToBinary(num)
print(z.count(1))
