s= input("""Enter list elements separated by comma(",")\n""" )
a_list=list(map(int,s.split(",")))
n=len(a_list)
for i in range(0,n):
	for j in range(0,n-i-1):
		if(a_list[j]>a_list[j+1]):
			a_list[j],a_list[j+1]=a_list[j+1],a_list[j]
			
print(a_list)
