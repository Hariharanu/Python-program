n,m,u=int(input()),[],[]
if n<1000000:
    m=input().split(" ")[:n]
    m.sort(reverse=False)
    u=input().split(" ")[:n]
    u.sort(reverse=False)
    if m==u:
    	print("Yes")
    else:
    	print("False")
 
