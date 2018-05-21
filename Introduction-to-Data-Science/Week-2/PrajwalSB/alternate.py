n= int(input("Enter: "))
lists=[]
for i in range(0,n):
	x=int(input())
	lists.append(x)
print(len(lists))
print("original list")
print(lists)
print("new list")
for i in range(1,n,2):
	del lists[(i+1)//2]
print(lists)
