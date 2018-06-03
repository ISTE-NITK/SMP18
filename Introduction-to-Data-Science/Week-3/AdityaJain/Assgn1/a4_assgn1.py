#!/usr/bin/python3 
import os

s=input('Input file name - ')
p=os.getcwd()
path=p+'/'+s
try :
    fil=open(path,'r+')
    l=fil.readlines()
except IOError :
    print('Error opening the file')
else :
    l.reverse()
    fil.seek(0,0)
    fil.writelines(l)
