
#Selection sort

n=int(input('Enter number of elements: '))

l=[]

for i in range(n):
    x=int(input('Enter number %d: '%(i+1)))
    l.append(x)

print()

for i in range(n-1):
    Min=min(l[i:])
    Min_index=l[i:].index(Min)+i
    l[i],l[Min_index]=Min,l[i]
    print('List after pass',i+1,':',l)

print ()
print ('Final Sorted List:',l)
