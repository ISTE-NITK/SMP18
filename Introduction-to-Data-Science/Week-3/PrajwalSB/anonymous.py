d={0:3,1:2,2:1,3:0}
dict={}
n=int(input("Enter : "))
print("Enter respective integer key and values ")
for i in range(0,n):
	key=int(input())
	dict[key]=int(input())
#for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k)):
 #   print "%s: %s" % (key, value)
output=sorted(dict.items(), key = lambda x : x[1]  )
print(output)
