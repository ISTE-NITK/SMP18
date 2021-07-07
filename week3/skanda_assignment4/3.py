

l=[1,2,3,4,5]

print('Following is a list:',l)

print('Trying to access element at index 10: ')

try:
    print('Element at index 10:',l[10])
   
except IndexError:
    print('Index Error!')


print('5 % 0 = ')

try:
    print(5%0)     
     
except ZeroDivisionError:
    
    print('ZeroDivisionError!')


print('x not defined, x = ')

try:
    print(x)

except NameError:
    print('NameError!')
