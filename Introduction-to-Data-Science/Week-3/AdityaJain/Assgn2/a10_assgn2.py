#!/usr/bin/python3 
import collections

class Person():
    def __init__(self,fn,ln,phn,email):
        self.__first_name=fn
        self.__last_name=ln
        self.__phone_number=phn
        self.__email=email
        return
    @property
    def first_name(self):
        return self.__first_name
    @property
    def last_name(self):
        return self.__last_name
    @property 
    def phone_number(self):
        return self.__phone_number
    @property
    def email(self):
        return self.__email
    def __str__(self):
        return '%s %s'%(self.__last_name,self.__first_name)
    
    def __repr__(self):
        return self.__str__()

class address_book():
    def __init__(self):
        self.__addrList=[]
        self.__noe=0
        self.__lnTable=collections.defaultdict(set)
        self.__fnTable=collections.defaultdict(set)
        return

    def addcontact(self,contact):
        self.__addrList.append(contact)
        self.__lnTable[contact.last_name].add(self.__noe)
        self.__fnTable[contact.first_name].add(self.__noe)
        self.__noe=self.__noe+1
        return

    def lookup_contact(self,ln,fn=None):
        matchset=self.__lnTable[ln]
        if(fn is not None):
            matchset=matchset & self.__fnTable[fn]
        if (len(matchset)==0):
            print('No match found')
        else:
            print('Matches Found :')
            for i in matchset:
                print(self.__addrList[i])
        return

yPages=address_book()
for i in ["Aditya Jain",'Aditya Rastogi','Mohit Bhasi','Ankit Jain','Shankaran Shrama','Mohit Mehta','Shweta Sharma','Kalyani Awasthi','Jyoti Mehta'] :
    fn,ln=i.split()
    yPages.addcontact(Person(fn,ln,'8000110011',['blahblah@bleh.bleh','lollol@lel.lel']))

yPages.lookup_contact('Jain')
print()
yPages.lookup_contact('Sharma','Kalyani')
print()
yPages.lookup_contact('Dwivedi')
print()
yPages.lookup_contact('Jain','Shankaran')
print()
yPages.lookup_contact('Dwi','Aditya')
print()
yPages.lookup_contact('Bhasi','Mohit')
