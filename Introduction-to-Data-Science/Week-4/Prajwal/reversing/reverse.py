file=open("input.txt",'r+')
last=file.seek(0,2)
lis=[0]
ctr=0
file.seek(0,0)
i=0
while i<last:
	file.readline()
	i=file.tell()
	lis.append(i)
	ctr+=1
f=open("output.txt",'w+')
dummy=ctr
for i in range(dummy,0,-1):
	file.seek(lis[i-1],0)
	print(file.readline(),end="")
	# below code is for writing it on another file called output
	file.seek(lis[i-1],0)
	f.write(file.readline())

file.close()
f.close()
	
