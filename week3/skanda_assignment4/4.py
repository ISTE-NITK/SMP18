
fp=open('reverse.txt','w')

op='y'
while op=='y' or op=='Y':
    line=input('Enter a line into the file: ')
    fp.write(line+'\n') 
    op=input('Want to enter more content? : ')


fp.close()


fp=open('reverse.txt','r')

fp.seek(0,2)
end=fp.tell()
fp.seek(0,0)

content=[]
line=fp.readline()

while fp.tell()!=end:
    content.append(line)
    line=fp.readline()


content.append(line)

#print('Content: ',content)

fp.close()

content.reverse()

fp=open('reverse.txt','w')

for i in content:
    fp.write(i)

print('The File has been reversed.')



