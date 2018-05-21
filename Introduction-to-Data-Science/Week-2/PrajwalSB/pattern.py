n= int(input("Enter: "))
for i in range(1,(n+1)):
	for j in range(n,i,-1):
		print("  ",end="")
	for k in range(1,i):
		print("* ",end="")
	for l in range(0,i):
		print("* ",end="")
	print()

for i in range(n-1,0,-1):
	for j in range(0,n-i):
		print("  ",end="")
	for k  in range(1,(i*2)):
		print("* ",end="")
	print()
	

