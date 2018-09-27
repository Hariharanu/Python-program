n,c=int(input()),0
n1=list(map(int,input().split(" ")))
n2=list(map(int,input().split(" ")))
for i in range(0,len(n1)):
	if n1[i]==n2[0]:
		m=i
for j in range(m+1,len(n1)):
	c=c+1
	if n1[j]==n2[1]:
		break
c=0
for j in range(m-1,0,-1):
	c=c+1
	if n1[j]==n2[1]:
		break
print(c)
