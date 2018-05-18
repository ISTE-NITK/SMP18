
n=int(input('Enter number of elements: '))

l=[]  #empty list

for i in range(n):
    x=input('Enter element %d: ' % (i+1))
    l.append(x)

print('Original list:',l)

l=l[::2]

print('New list:',l)


