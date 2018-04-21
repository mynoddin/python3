# Classes and Object 

class Person:
    # this variable are private 
    __name = ''
    __email = ''
    
    #its a constructor 
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        
    def set_name(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_email(self, email):
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)    

brad = Person("Md Mynoddin", "example@mail.com")

#inheritance 

class Customer(Person): 
    __balance = 0
    
    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)
     
        
    def set_balance(self, balance):
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def toString(self):
        return '{} has a balance of {} and can be contacted at {}'.format(self.__name, self.__balance, self.__email)
    

john = Customer("Mynoddin", "example@mail.com", 9500)

print(john.toString())

john.set_balance(400)

print(john.toString())

kate = Customer("Kate Smith", "example@mail.com", 5000)

print(kate.toString())