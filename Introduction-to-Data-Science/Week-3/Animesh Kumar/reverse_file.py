import os
f= open("text1.txt",'w+')
f.write("Hello\nI\nAm playing")
f.seek(0,0)
print(f.readlines())
f.close()                                                                             
fp= open("text1.txt",'r')
k= fp.readlines()                                                                     
fp.close()                                                                            
k=k[::-1]
k[0]=k[0]+"\n"
k[-1]=k[-1][:-1]
fm= open("text1.txt",'w+')                                                            
for t in k:                                                                           
    fm.write(t)                                                                   
fm.seek(0,0)                                                                          
print(fm.readlines())                                                                 
fm.close()        