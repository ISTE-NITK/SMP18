
class Person:
    def __init__(self,first_name,last_name,phone_number,*email):
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.email=email


class Address_book:
    def __init__(self):
        self.contacts=[]

    def add_contact(self,first_name,last_name,phone_number,*email):
        temp=Person(first_name,last_name,phone_number,*email)
        self.contacts.append(temp)

    def lookup_contact(self,last_name,first_name=None):
        for i in self.contacts:
            if first_name==None and i.last_name==last_name:
                self.print_contact(i)
            elif i.first_name==first_name and i.last_name==last_name:
                self.print_contact(i)

    def print_contact(self,person):
        print('First Name:',person.first_name)
        print('Last Name:',person.last_name)
        print('Phone Number:',person.phone_number)
        print('Email:',person.email)
        print()     
                     



# a-An object of Address_book class
a=Address_book()

#adding contacts
a.add_contact('abcd','qwerty','9786432188','abcd@gmail.com','abcd.qwert@gmail.com')
a.add_contact('abcy','qwerty','7777755555','qwerty.abcy@gmail.com')
a.add_contact('cdefg','tyuio','1234567890','cde.tyu@gmail.com','cdefg.ty@gmail.com')
a.add_contact('asdfgh','fghjk','9008889900','asdfgh@gmail.com','fghy@gmail.com')

#searching using only last name
a.lookup_contact('qwerty')

#searching using first name and last name
a.lookup_contact('fghjk','asdfgh')



