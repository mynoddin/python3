#import entire module 
import greet 

greet.sayHello("Tim")

count = 1 
while count <= 10:
    print ("This is  task ", count)
    count = count + 1; 
    
#import a specific element 
from greet import sayGoodbye

sayGoodbye("Tim")