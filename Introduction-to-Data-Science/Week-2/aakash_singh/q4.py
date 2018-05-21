#q4
#removes additional occurences in the list

inp=input("Enter list of integers with spaces between them: ")
numbers = [int(i) for i in inp.split()]

temp=list(numbers)
numbers.clear()

for i in temp:
    if i not in numbers:
        numbers.append(i)

print('modified list: ')
print(numbers)