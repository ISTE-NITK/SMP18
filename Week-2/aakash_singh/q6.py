#q6 diamond pattern code

try:
    n = int(input("Enter size of diamond: "))
except:
    print("run the program again and enter a positive integer")
    exit()

if n < 0:
    exit()

for i in range(1,n+1): #prints upper half of diamond
    print(' ' * (n-i) + '*' * (2 * i - 1))
for i in range(n-1,0,-1): #prints lower half of diamond
    print(' ' * (n-i) + '*' * (2 * i - 1))