list = input('enter the elements in the list').split()
n=len(list)
for i in range(0,n,2):
	del list[i]
print(list)
