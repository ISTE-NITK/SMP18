list1=[]
n=int(input("enter the no:of items in list\n"))
print("enter the items")
for i in range(0,n):
	list1.append(int(input()))
l=len(list1)
for i in range(0,l):	
	if i>=l:
		break
	del list1[i]
	l-=1
print(list1)

