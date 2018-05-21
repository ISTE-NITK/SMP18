n=int(input("Enter The value of N\n"))
print (n)
for i in range(0,n):
	for k in range(n-i-1,0,-1):
		print(" ",end="")
	for j in range(0,2*i+1):
		print("*",end="")
	print("\n")
for i in range(n-2,-1,-1):
	for k in range(n-1-i,0,-1):
		print(" ",end="")
	
	for j in range(0,2*i+1):
		print("*",end="")
	print("\n")

