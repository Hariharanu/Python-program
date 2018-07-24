n=input()
v=['a','e','i','o','u']
char=[]
for i in n:
	if i not in v:
		char.append(i)
char=list(reversed(char))
print("".join(char))
