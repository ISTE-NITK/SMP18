s= input("""Enter list elements separated by comma(",")\n""" )
list_a=list(map(int,s.split(",")))
for i in list_a:
	list_a.remove(i)
print(list_a)
