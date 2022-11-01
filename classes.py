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
        

brad = Person("Md Mynoddin", "mynosin@email.com")
#brad.set_name("Md Mynoddin")
#brad.set_email("mynosin@email.com")

print(brad.get_name())
print(brad.get_email())

print(brad.toString())








