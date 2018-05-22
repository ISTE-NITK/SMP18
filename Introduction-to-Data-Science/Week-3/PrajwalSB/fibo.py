n= int(input("Enter : "))

if n==1:
	print(0)
else:
	print('0' +' '+ '1 ',end="")
	a=0 
	b=1
	for i in range(0,n-2):
		c=a+b
		print(c,end="")
		print(" ",end="")
		a=b 
		b=c

