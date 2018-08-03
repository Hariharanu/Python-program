def play_41(n,k):
	i=n
	while(i>1):
		i=n%k
		n//=2
	if i==0:
		print("Yes")
	else:
		print("No")
n=list(map(int,input().split(" ")))
play_41(n[0],n[1])
