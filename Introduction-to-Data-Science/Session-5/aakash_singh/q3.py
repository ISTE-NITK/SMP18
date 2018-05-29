try:
    n=int(input('enter a number: '))
except ValueError:
    print('please try again and input a number')
    exit()

try:
    print(100/n)
except ZeroDivisionError:
    print('cant divide by zero')
    exit()