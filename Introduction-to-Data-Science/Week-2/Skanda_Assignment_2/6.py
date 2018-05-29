
n=int(input('Enter n: '))


for i in range(2*n-1):
    if i<n:
        print(' '*(n-1-i)+'*'*(2*i+1))
    else:
        print(' '*(i+1-n)+'*'*(2*(2*n-i-1)-1))
        

