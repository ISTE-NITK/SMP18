class person:
    def __init__(self, first_name='', last_name='', phone_number='', email=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        s = self.first_name+' '+self.last_name+'\n'+self.phone_number+'\n'
        for e in self.email:
            s += e+'\n'
        return s.strip()

    def __repr__(self):
        return self.__str__()


class address_book:
    def __init__(self):
        self.ad_book = []

    def add_contact(self):
        newPerson = person()
        newPerson.first_name = input('first name: ')
        newPerson.last_name = input('last name: ')
        newPerson.phone_number = input('phone number: ')
        for i in range(int(input('enter number of email: '))):
            newPerson.email.append(input('email {}: '.format(i+1)))
        self.ad_book.append(newPerson)

    def lookup_contact(self, ln):
        for i in self.ad_book:
            if ln == i.last_name:
                print(i)
                return