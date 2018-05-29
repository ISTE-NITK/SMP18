

from operator import itemgetter

def sort_val(dict):
    items_list=list(dict.items())
    print('Original Dictionary:',items_list)
    items_list.sort(key=itemgetter(1))
    print ('Value sorted Dictionary:',items_list)


n=int(input('Enter size: '))
dictionary={} 

for i in range(n):
    a,b=input('Enter key,value of element %d: ' %(i+1)).split()
    a=int(a)
    b=int(b)
    dictionary[a]=b


sort_val(dictionary)
    
