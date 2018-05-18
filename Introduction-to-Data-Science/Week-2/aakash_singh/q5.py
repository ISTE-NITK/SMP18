#q5

inp=input("Enter list of integers with spaces between them: ")
numbers = [int(i) for i in inp.split()]
n=len(numbers)
i,j=0,0   #bubble sort
while i < n-1:
    j=0
    while j < n-1-i:
        if numbers[j] > numbers[j+1]:
            numbers[j] , numbers[j+1] = numbers[j+1] , numbers[j]
        j+=1
    i+=1

print("sorted array: ")
print(numbers)