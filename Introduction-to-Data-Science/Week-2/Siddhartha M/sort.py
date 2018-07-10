#Bubble sort
list1=[]
l=int(input("enter no:of items\n"))
print("enter int items")
for i in range(0,l):
	list1.append(int(input()))
n=len(list1)
for i in range(0,n-1) :
	for j in range(0,n-i-1):
		if list1[j] > list1[j+1]:
			temp=list1[j]
			list1[j]=list1[j+1]
			list1[j+1]=temp
print(list1)
