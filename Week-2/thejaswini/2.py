list=input('enter the elements of list').split()
n=len(list)
list.sort(key=len)
print(list)
