def fibbonaci(n):
    if n <=0:
        return ("invalid input")
    else:
        first = 0
        second = 1
        k=[0,1]
        if n==1:
            return(k[0:1])
        elif n== 2:
            return(k)
            
        else:
            third = 0
            for i in range(0,n-2):
                third = first + second
                first = second
                second = third
                k.append(third)
            return k        
print(fibbonaci(4))
  
    