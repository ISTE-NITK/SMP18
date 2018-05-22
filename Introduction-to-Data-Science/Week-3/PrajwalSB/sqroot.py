n=int(input("Enter a number: "))
for i in range(0,n//2 +1):
	if i*i==n:
		print(i)
		break
	if i*i>n:
		print("no perfect square")
		break
