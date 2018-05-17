n=int(input("enter the value of n"))
for i in range(0,n):
	for j in range(0,(n-1-i)):
		print(" ",end="")
	for k in range(0,(i*2+1)):
		print("*",end="")
	print(" ")
for i in range(1,n):
	for j in range(0,i):
		print(" ",end="")
	for k in range(0,(n-i)*2-1):
		print("*",end="")
	print(" ")
	
