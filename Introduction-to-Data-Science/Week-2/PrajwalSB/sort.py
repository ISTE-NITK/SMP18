n= int(input("Enter: "))
lists=[]
for i in range(0,n):
	x=int(input())
	lists.append(x)

for i in range(0,n-1):
	for j in range(0,n-1-i):
		if lists[j] > lists[j+1]:
			temp =lists[j]
			lists[j]=lists[j+1]
			lists[j+1]=temp

print(lists)
