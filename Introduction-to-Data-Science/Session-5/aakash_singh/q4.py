import sys

try:
    file = open(sys.argv[1],'r')
except:
    print('file doesnt exist')
    exit()

lines=file.read().split('\n')
file.close()
for line in lines[::-1]:
    print(line.strip())